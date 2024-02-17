def findinFiles(filename):
    import configparser
    config = configparser.ConfigParser()
    config.read('/etc/mkt.conf')
    default_shell = (config['Mkt']['ShellProgram']).strip()

    import subprocess,os
    command = "find /Tools/ -type f -iname '*%s*' -not -name '*\.mkt' " % (filename[0])
    status,output_str = subprocess.getstatusoutput(command)
    files = output_str.split()

    # add filter
    for search in filename[1:]:
        # print("[*] Filtering : %s" % search)
        tmp_search = []
        search = search.strip().lower()
        for file in files:
            if file.lower().find(search) != -1:
                tmp_search.append(file)
        files = tmp_search

    # result
    if (len(files) == 1):
        print ("[*] Goto: %s" % (files[0]))
        os.chdir(os.path.dirname(files[0]))
        os.system(default_shell)
        return

    if (len(files) == 0):
        print("[!] Not Founded!")
        return

    # more files need to select
    def show_list():
        for index,file in enumerate(files):
            print("[%s] %s" % (index,file.replace("/Tools/","")))
    read_input = None
    show_list()
    print("Tips: input 'l' can list again")
    while True:
        user_input = input(" Go to : ").strip()
        if user_input == "l" : show_list()
        if user_input.isdigit(): 
            if (int(user_input) >= 0) and (int(user_input) <= len(files) - 1):
                print ("[*] Selected: %s" % (files[int(user_input)]))
                os.chdir(os.path.dirname(files[int(user_input)]))
                os.system(default_shell)
                break