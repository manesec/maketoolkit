import os,sys
import subprocess
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import time 

import configparser
config = configparser.ConfigParser()
config.read('/etc/mkt.conf')

max_worker = int(config['MktSearch']['SearchThread'])
blacklistExt = config['MktSearch']['SearchBlackList'].split("|")
blacklistFile = config['MktSearch']['SearchBlackFile'].split("|")

def CHECK_TEXT_A_FILE(inputfile) -> bool:
    out = subprocess.getoutput("file '%s'" % (inputfile.replace("'","\'")))
    if (out.find("text")!=-1):
        return inputfile,True
    return inputfile,False

def ReIndex():
    if (os.getuid() != 0):
        print("[ERR] Please run as root user.")
        sys.exit(0)

    if (os.path.exists("/var/lib/mkt/Res/WhooshIndex")):
        os.system("rm -rf /var/lib/mkt/Res/WhooshIndex")

    os.chdir("/var/lib/mkt/Res")
    
    from pathlib import Path
    path = Path("/var/lib/mkt/Res/WhooshIndex")
    path.mkdir(parents=True, exist_ok=True)

    begin_time = time.time()
    all_file_list = ()

    for dirpath, dirnames, filenames in os.walk("/var/lib/mkt/Res/Data"):
        for file in filenames:
            full_path = dirpath + "/" + file
            if (full_path.find("/.") != -1):
                continue
            all_file_list += (full_path,)

    print("[!] Found %s files." % (len(all_file_list)))

    # filter blacklist extension
    tmp_file_list = ()

    for file_path in all_file_list:
        Have_Blackext = False
        for blackext in blacklistExt:
            if (blackext.strip() == ""):
                continue
            if (file_path[-len(blackext):] == blackext):
                Have_Blackext = True
        if not (Have_Blackext):
            tmp_file_list += (file_path,)

    all_file_list = tmp_file_list

    # Bad Filename
    from pathlib import Path
    tmp_file_list = ()

    for file_path in all_file_list:
        Have_BlackFile = False
        for blackfile in blacklistFile:
            blackfile = blackfile.strip()
            if (blackfile == ""):
                continue
            if (Path('/root/dir/sub/file.ext').stem == blackfile):
                Have_BlackFile = True
        if not (Have_BlackFile):
            tmp_file_list += (file_path,)
    all_file_list = tmp_file_list

    print("[!] Filtered Black list file extension, Still have %s files." % (len(all_file_list)))
    

    # filter exclude readable text
    print("[*] Filtering text only files ...")
    executor = ThreadPoolExecutor(max_workers=max_worker)
    all_task = []
    for file_path in all_file_list:
        all_task.append(executor.submit(CHECK_TEXT_A_FILE,file_path))

    tmp_file_list = ()
    wait(all_task,return_when=ALL_COMPLETED)
    for task in all_task:
        file_path,result = task.result()
        if (result):
            tmp_file_list += (file_path,)
    all_file_list = tmp_file_list
    
    print("[*] Indexing %s files ... "% (len(all_file_list)))
    print("    Please wait some few minutes ...")

    from whoosh.index import create_in
    from whoosh.fields import ID, KEYWORD, Schema

    schema = Schema(path=ID(stored=True), content=KEYWORD())
    ix = create_in("WhooshIndex", schema)
    writer = ix.writer()

    for file_path in all_file_list:
        filestr = open(file_path,'r',encoding="iso-8859-1").read()
        writer.add_document(path=file_path,content=filestr)

    writer.commit()

    print("[*] Finished, take %s seconds." % (round(time.time() - begin_time,2)) )

def Search_mult(searchstr):
    #print("[*] Using whoosh search engine...")

    tmp_searchstr = ""
    for searchs in searchstr:
        tmp_searchstr += "*%s* " % (searchs)

    os.chdir("/var/lib/mkt/Res")

    if not (os.path.exists("/var/lib/mkt/Res/WhooshIndex")):
        print("[*] Look like the frist time to use, there not index.")
        if (os.getuid() == 0):
            print("[*] Trying to re-indexing ...")
            ReIndex()
        else:            
            print("Please run as sudo to indexing search DB.")
            print("  $ sudo mkt db reindex")
            sys.exit(0) 

    from whoosh.index import open_dir
    from whoosh.qparser import MultifieldParser

    file_list = ()
    ix = open_dir("WhooshIndex")
    with ix.searcher() as searcher:
        query = MultifieldParser(["path","content"], ix.schema).parse(tmp_searchstr)
        results = searcher.search(query, limit=None)
        for result in results:
            file_list += (result["path"],)        
    return file_list
        
    