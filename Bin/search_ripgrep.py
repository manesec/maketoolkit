def MKT_CHECK_COMMAND(command):
    import subprocess
    code,_ =  subprocess.getstatusoutput("command -v " + command)
    if code == 0:
        return True
    else:
        return False

def Search_single(file,searchstr) -> bool:
    import subprocess,sys
    if not MKT_CHECK_COMMAND("rg"):
        print("[ERROR] rg command not exits on your system, please check your PATH.")
        sys.exit(0)
    searchstr = searchstr.replace("'","\'")
    command = "rg --color never -m 1 -iLl -F '%s' '%s'"  % (searchstr,file)
    status,output_str = subprocess.getstatusoutput(command)
    if (status == 0) :
        return (file,True)
    return (file,False)

def Search_mult(searchstr):
    #print("[*] Using ripgrep search engine...")
    import subprocess,sys
    if not MKT_CHECK_COMMAND("rg"):
        print("[ERROR] rg command not exits on your system, please check your PATH.")
        sys.exit(0)

    return_list = ()
    searchstr = searchstr.replace("'","\'")
    command = "rg --color never -m 1 -F -iLl '%s' '/var/lib/mkt/Res/Data/'" %(searchstr)

    status,output_str = subprocess.getstatusoutput(command)

    if (status == 0) :
        for l in output_str.split('\n'):
            if (l.strip() == ""):
                continue
            return_list += (l,)

    return return_list

def Search_inList(input_list,searchstr,searchstrstack = ""):
    from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
    
    import configparser
    config = configparser.ConfigParser()
    config.read('/etc/mkt.conf')
    max_worker = int(config['MktSearch']['SearchThread'])

    new_stdout_list = ()
    def sub_search_thread (f,searchstr):
        return Search_single(f,searchstr)

    executor = ThreadPoolExecutor(max_workers=max_worker)
    all_task = []
    for f in input_list:
        all_task.append(executor.submit(sub_search_thread,f,searchstr))
    
    wait(all_task,return_when=ALL_COMPLETED)
    for task in all_task:
        taskname,result = task.result()
        if (result):
            if (taskname not in new_stdout_list):
                new_stdout_list += (taskname,)
                continue
        
        if (taskname.lower().find(searchstr.lower()) !=-1):
            if result not in new_stdout_list:
                new_stdout_list += (taskname,)
                continue

    return new_stdout_list