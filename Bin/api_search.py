import sys,os,time,subprocess
import json
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

import configparser
config = configparser.ConfigParser()
config.read('/etc/mkt.conf')

max_worker = int(config['MktSearch']['SearchThread'])
search_engine = config['MktSearch']['SearchEngine'].lower().strip()
blacklistExt = config['MktSearch']['SearchBlackList'].split("|")
blacklistFile = config['MktSearch']['SearchBlackFile'].split("|")
max_result = int(config['DocServer']['MaxResult'])


# apply search and filter text only
traditionalSearchEngine = ["grep","ripgrep"]


isDebug = False

def Debug(obj):
    if isDebug :
        print(obj)


Debug("[*] Select search engine: %s" % (search_engine))

# ==========================================================================
#                              Some Function
# ==========================================================================

def MKT_CHECK_COMMAND(command):
    import subprocess
    code,_ =  subprocess.getstatusoutput("command -v " + command)
    if code == 0:
        return True
    else:
        return False

def CHECK_TEXT_A_FILE(inputfile) -> bool:
    out = subprocess.getoutput("file '%s'" % (inputfile.replace("'","\'")))
    if (out.find("text")!=-1):
        return inputfile,True
    return inputfile,False

def CHECK_TEXT_FILE(InputList):
    executor = ThreadPoolExecutor(max_workers=max_worker)
    all_task = []
    for file_path in InputList:
        all_task.append(executor.submit(CHECK_TEXT_A_FILE,file_path))

    tmp_file_list = ()
    wait(all_task,return_when=ALL_COMPLETED)
    for task in all_task:
        file_path,result = task.result()
        if (result):
            tmp_file_list += (file_path,)
    return tmp_file_list


# ==========================================================================
#                              Search Function
# ==========================================================================

def MKT_DB_SEARCH():
    global searchWorldList
    global showFileList
    global history_stack
    global out_stdout_list
    global timeused

    import subprocess
    if (len(sys.argv) != 3):
        Debug("[ERROR] Invalid parameter")
        Debug("    Usage: mkt search <string>")
        sys.exit(0)

    Debug("[*] Searching LocalDB ...")
    

    filter_title = ()
    searchWorldList = []


    # A || B
    command_or = []
    if (sys.argv[2].find("||")):
        Debug("input command find ||")
        command_or = sys.argv[2].split("||")
        Debug("command_or => " + str(command_or))

        for user_input in command_or:
            user_input = user_input.strip()
            if user_input.startswith("[") and user_input.endswith("]") :
                user_input = user_input[1:-1]
                filter_title += (user_input,)
            else:
                searchWorldList.append(user_input)

        Debug("filter_title => " + str(filter_title))
    else:
        searchWorldList = sys.argv[2].strip()

    searchWorldList = sorted(searchWorldList,key=len)
    searchWorldList.reverse()
    Debug("searchWorldList => " + str(searchWorldList) )

    ## -- Begin to search -- ##
    #  [[search_stacks,input_list]]

    out_stdout_list = ()

    # traditionalSearchEngine
    if search_engine in traditionalSearchEngine :
        frist_search = True
        for searchstr in searchWorldList:
            if frist_search:
                # Grep
                Debug("[*] Frist search with %s ..." % (searchstr))
                from importlib.machinery import SourceFileLoader
                search_bin = "/var/lib/mkt/Bin/search_%s.py" % search_engine
                out_stdout_list = SourceFileLoader("search_%s" % (search_engine), search_bin).load_module().Search_mult(searchstr)

                # Find
                Debug("[*] Using find to search filename ...")
                searchstr = searchstr.replace("'","\'")
                command = "find /var/lib/mkt/Res/Data/ -type f -iname '*%s*'" % searchstr
                status,output_str = subprocess.getstatusoutput(command)
                for l in output_str.split('\n'):
                    if (l.find("/.")!=-1):
                        continue
                    if (l.strip() == ""):
                        continue                
                    if l not in out_stdout_list:
                        out_stdout_list += (l,)

                # Bad Extensions
                Debug("[*] Filting bad extensions ...")
                tmp_file_list = ()
                for file_path in out_stdout_list:
                    Have_Blackext = False
                    for blackext in blacklistExt:
                        blackext = blackext.strip()
                        if (blackext == ""):
                            continue
                        if (file_path[-len(blackext):] == blackext):
                            Have_Blackext = True
                    if not (Have_Blackext):
                        tmp_file_list += (file_path,)
                out_stdout_list = tmp_file_list

                # Bad Filename
                from pathlib import Path
                Debug("[*] Filting bad filename ...")
                tmp_file_list = ()

                for file_path in out_stdout_list:
                    Have_BlackFile = False
                    for blackfile in blacklistFile:
                        blackfile = blackfile.strip()
                        if (blackfile == ""):
                            continue
                        if (Path('/root/dir/sub/file.ext').stem == blackfile):
                            Have_BlackFile = True
                    if not (Have_BlackFile):
                        tmp_file_list += (file_path,)
                out_stdout_list = tmp_file_list

                # Text only
                Debug("[*] Filtering exclude text only ..." )
                out_stdout_list = CHECK_TEXT_FILE(out_stdout_list)
                
                # No result and exit
                if (len(out_stdout_list)==0):
                    Debug("[!] No result.")
                    sys,exit(0)

                frist_search = False
                continue

            # Second Search
            Debug("[*] Filtering %s ..." % (searchstr))

            from importlib.machinery import SourceFileLoader
            search_bin = "/var/lib/mkt/Bin/search_%s.py" % search_engine
            out_stdout_list = SourceFileLoader("search_%s" % (search_engine), search_bin).load_module().Search_inList(out_stdout_list,searchstr)

            if (len(out_stdout_list)==0):
                Debug("[!] No result")
                sys,exit(0)

    else:
        # non traditionalSearchEngine
        from importlib.machinery import SourceFileLoader
        search_bin = "/var/lib/mkt/Bin/search_%s.py" % search_engine
        out_stdout_list = SourceFileLoader("search_%s" % (search_engine), search_bin).load_module().Search_mult(searchWorldList)

        Debug("[*] Filting bad extensions ...")
        tmp_file_list = ()
        for file_path in out_stdout_list:
            Have_Blackext = False
            for blackext in blacklistExt:
                blackext = blackext.strip()
                if (blackext == ""):
                    continue
                if (file_path[-len(blackext):] == blackext):
                    Have_Blackext = True
            if not (Have_Blackext):
                tmp_file_list += (file_path,)
        out_stdout_list = tmp_file_list

        # Bad Filename
        from pathlib import Path
        Debug("[*] Filting bad filename ...")
        tmp_file_list = ()

        for file_path in out_stdout_list:
            Have_BlackFile = False
            for blackfile in blacklistFile:
                blackfile = blackfile.strip()
                if (blackfile == ""):
                    continue
                if (Path('/root/dir/sub/file.ext').stem == blackfile):
                    Have_BlackFile = True
            if not (Have_BlackFile):
                tmp_file_list += (file_path,)
        out_stdout_list = tmp_file_list


    ## -- End to search -- ##



    Debug("out_stdout_list => " + str(len(out_stdout_list)))
    for f_title in filter_title:
        tmp_list = []
        for obj in out_stdout_list:
            if (f_title.lower() in obj.lower()):
                tmp_list.append(obj)
        Debug("len(tmp_list) => " + str(len(tmp_list)))
        out_stdout_list = tmp_list


    Debug("out_stdout_list => " + str(len(out_stdout_list)))



    out_stdout_list = out_stdout_list[:max_result]
    out_stdout_list = list(out_stdout_list)
    out_stdout_list = [x.replace("/var/lib/mkt/Res/Data/","") for x in out_stdout_list]

    print (json.dumps(out_stdout_list))


MKT_DB_SEARCH()