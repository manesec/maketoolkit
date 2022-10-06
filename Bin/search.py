import sys,os,time,subprocess
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

import configparser
config = configparser.ConfigParser()
config.read('/etc/mkt.conf')

max_worker = int(config['MktSearch']['SearchThread'])
search_engine = config['MktSearch']['SearchEngine'].lower().strip()
blacklistExt = config['MktSearch']['SearchBlackList'].split("|")
blacklistFile = config['MktSearch']['SearchBlackFile'].split("|")

# apply search and filter text only
traditionalSearchEngine = ["grep","ripgrep"]

print("[*] Select search engine: %s" % (search_engine))


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
    if (len(sys.argv) < 3):
        print("[ERROR] Invalid parameter")
        print("    Usage: mkt search <string>")
        sys.exit(0)

    print("[*] Searching LocalDB ...")
    searchWorldList = sys.argv[2:]
    searchWorldList = sorted(searchWorldList,key=len)
    searchWorldList.reverse()

    ## -- Begin to search -- ##
    #  [[search_stacks,input_list]]
    history_stack = []

    # Count count count
    begin_time = time.time()
    end_time = time.time()
    timeused = round(end_time - begin_time,2)

    out_stdout_list = ()

    # traditionalSearchEngine
    if search_engine in traditionalSearchEngine :
        frist_search = True
        for searchstr in searchWorldList:
            if frist_search:
                # Grep
                print("[*] Frist search with %s ..." % (searchstr))
                from importlib.machinery import SourceFileLoader
                search_bin = "/var/lib/mkt/Bin/search_%s.py" % search_engine
                out_stdout_list = SourceFileLoader("search_%s" % (search_engine), search_bin).load_module().Search_mult(searchstr)

                # Find
                print("[*] Using find to search filename ...")
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
                print("[*] Filting bad extensions ...")
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
                print("[*] Filting bad filename ...")
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
                print("[*] Filtering exclude text only ..." )
                out_stdout_list = CHECK_TEXT_FILE(out_stdout_list)
                
                # No result and exit
                if (len(out_stdout_list)==0):
                    end_time = time.time()
                    timeused = round(end_time - begin_time,2)
                    print("[!] No result, take %s seconds." % (timeused))
                    sys,exit(0)

                frist_search = False
                continue

            # Second Search
            print("[*] Filtering %s ..." % (searchstr))

            from importlib.machinery import SourceFileLoader
            search_bin = "/var/lib/mkt/Bin/search_%s.py" % search_engine
            out_stdout_list = SourceFileLoader("search_%s" % (search_engine), search_bin).load_module().Search_inList(out_stdout_list,searchstr)

            if (len(out_stdout_list)==0):
                end_time = time.time()
                timeused = round(end_time - begin_time,2)
                print("[!] No result, take %s seconds." % (timeused))
                sys,exit(0)

    else:
        # non traditionalSearchEngine
        from importlib.machinery import SourceFileLoader
        search_bin = "/var/lib/mkt/Bin/search_%s.py" % search_engine
        out_stdout_list = SourceFileLoader("search_%s" % (search_engine), search_bin).load_module().Search_mult(searchWorldList)

        print("[*] Filting bad extensions ...")
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
        print("[*] Filting bad filename ...")
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
    timeused = round(time.time() - begin_time,2)

    if (len(out_stdout_list) == 0):
        print("[!] No found on Local DB, take %s seconds." % (timeused))
        sys.exit(0)

    print("\n[*] Found that in the file, take %s seconds :"  % (timeused) )

    history_stack.append([searchWorldList,out_stdout_list])
    showFileList = [l for l in out_stdout_list]

    # Operation Function
    def OpNothing(_=""):
        pass

    def OpExit(_=""):
        sys.exit(0)

    def OpShowHelp(_=""):
        os.system("less /var/lib/mkt/Data/SearchHelp.txt")

    def Oplistoutput(_=""):
        print( "-" * 50 )
        index = 0
        for file in showFileList:
            print("[%s] %s" % (index,file.replace("/var/lib/mkt/Res/Data/","")))
            index += 1

    def OpFilterTitle(arg):
        global searchWorldList
        global showFileList
        global history_stack
        global out_stdout_list
        global timeused

        begin_time = time.time()

        if (len(arg) == 0):
            print("[ERROR] Please input your keyword!")
            return

        NewSearchWorldList = searchWorldList
        new_stdout_list = ()

        for keyword in arg:
            print("[*] Filtering title %s ..." % (keyword))
            for f in out_stdout_list:
                if (f.replace("/var/lib/mkt/Res/Data/","").lower().find(keyword.lower()) !=-1) :
                    if (f not in new_stdout_list):
                        new_stdout_list += (f,)

            NewSearchWorldList.append(keyword)

        if (len(new_stdout_list) == 0):
            print("[!] No found.")
            return
        
        history_stack.append([NewSearchWorldList,new_stdout_list])
        showFileList = [l for l in new_stdout_list]
        out_stdout_list = new_stdout_list
        searchWorldList = NewSearchWorldList
        Oplistoutput()

        end_time = time.time()
        timeused = round(end_time - begin_time,2)


    def OpBackStack(_=""):
        global searchWorldList
        global showFileList
        global history_stack
        global out_stdout_list

        if (len(history_stack) == 1):
            print("[!] Already on the top.")
        else:
            del history_stack[-1]
            searchWorldList, out_stdout_list = history_stack[-1]
            print("[*] Back to %s ..." % (len(history_stack) -1 ))
            showFileList = [l for l in out_stdout_list]
            Oplistoutput()

    def OpFilter(arg):
        global searchWorldList
        global showFileList
        global history_stack
        global out_stdout_list
        global timeused

        if (len(arg) == 0):
            print("[ERROR] Please input your keyword!")
            return

        NewSearchWorldList = searchWorldList
        Tmp_out_stdout_list = out_stdout_list
        begin_time = time.time()

        for newkeyword in arg:
            NewSearchWorldList.append(newkeyword)

        if search_engine in traditionalSearchEngine :
            for newkeyword in arg:
                print("[*] Filtering %s ..." % (newkeyword))
                from importlib.machinery import SourceFileLoader
                search_bin = "/var/lib/mkt/Bin/search_%s.py" % search_engine
                Tmp_out_stdout_list = SourceFileLoader("search_%s" % (search_engine), search_bin).load_module().Search_inList(Tmp_out_stdout_list,newkeyword)
        
        else:
            from importlib.machinery import SourceFileLoader
            search_bin = "/var/lib/mkt/Bin/search_%s.py" % search_engine
            Tmp_out_stdout_list = SourceFileLoader("search_%s" % (search_engine), search_bin).load_module().Search_mult(NewSearchWorldList)

            print("[*] Filting bad extensions ...")
            tmp_file_list = ()
            for file_path in Tmp_out_stdout_list:
                Have_Blackext = False
                for blackext in blacklistExt:
                    blackext = blackext.strip()
                    if (blackext == ""):
                        continue
                    if (file_path[-len(blackext):] == blackext):
                        Have_Blackext = True
                if not (Have_Blackext):
                    tmp_file_list += (file_path,)
            Tmp_out_stdout_list = tmp_file_list

        # final
        if (len(Tmp_out_stdout_list)==0):
            print("[!] No result.")
            return

        out_stdout_list = Tmp_out_stdout_list
        searchWorldList= NewSearchWorldList
        history_stack.append([searchWorldList,Tmp_out_stdout_list])
        showFileList = [l for l in Tmp_out_stdout_list]
        Oplistoutput()

        end_time = time.time()
        timeused = round(end_time - begin_time,2)

    Oplistoutput()

    # Operation Mode
    while (True):
        input_str = input("  (h)elp - %s :" % (timeused))
        input_str = input_str.strip().lower()

        # open doc
        if (input_str.isdigit()):
            input_number = int(input_str)
            if (input_number > len(showFileList)-1):
                print("[ERROR] Out of range.")
            else:
                doc_path = showFileList[input_number]
                print("[*] Opening %s ..." % (doc_path.replace("/var/lib/mkt/Res/Data/","")))
                if ((os.path.basename(doc_path).lower().find(".md")!= -1) and (MKT_CHECK_COMMAND("glow"))):
                    os.system("glow -p '%s'" % (doc_path))
                    Oplistoutput()
                else:
                    less_param = "/"
                    for searchstr in sys.argv[2:]:
                        less_param += "%s|" % (searchstr.strip())
                    less_param = less_param[:-1]
                    os.system("less +1 +'%s'  '%s'" % (less_param, doc_path) )
                    Oplistoutput()
            continue

        # Reading command
        if (input_str == ""):
            continue

        input_strargv = []
        if (len(input_str.split(" ")) != 1):
            for argv in input_str.split(" "):
                if argv.strip() == "":
                    continue
                input_strargv.append(argv)

        if len(input_strargv) >= 2:
            input_strargv = input_strargv[1:]
        else:
            input_strargv = []

        SelectFunction = {
            "h" : OpShowHelp,
            "l" : Oplistoutput,
            "q" : OpExit,
            "t" : OpFilterTitle,
            "b" : OpBackStack,
            "f" : OpFilter
        }

        SelectFunction.get(input_str.split(" ")[0],OpNothing)(input_strargv)
        
        continue
