import configparser
import subprocess,os
from pyfzf.pyfzf import FzfPrompt
import shutil

def copyAndfindinFiles(filename):
    #print(filename)

    if not filename[1]:
        filename[1] = os.getcwd()

    filename, target = filename

    config = configparser.ConfigParser()
    config.read('/etc/mkt.conf')
    default_shell = (config['Mkt']['ShellProgram']).strip()
    fzf = FzfPrompt()
    
    if (not filename):
        command = "find /Tools/ -type f -not -name '*\.mkt' -not -path '*/.git/*' " 
        status,output_str = subprocess.getstatusoutput(command)
        files = output_str.split('\n')

        if (len(files) == 0):
            print("[!] Not such files, please install some tools.")
            return

        userSelect = fzf.prompt(files)
        if userSelect:
            userSelect = userSelect[0]
            print ("[*] Copying %s --> %s ..." % (userSelect, target))
            os.system("cp '%s' '%s' " % (userSelect,target))
            return
        else:
            print("[!] User cancel select.")

    else:
        command = "find /Tools/ -type f -iname '*%s*' -not -name '*\.mkt' -not -path '*/.git/*' " % (filename[0])
        status,output_str = subprocess.getstatusoutput(command)

        if output_str.strip() == '':
            print("[!] Not Found!")
            return

        files = output_str.split('\n')

        # add filter
        tmp_search = []
        for file in files:
            if filename.strip().lower() in file.lower():
                tmp_search.append(file)
        files = tmp_search
        

        # result
        if (len(files) == 1):
            userSelect = files[0]
            print ("[*] Copying %s --> %s ..." % (userSelect, target))
            os.system("cp '%s' '%s' " % (userSelect,target))
            return

        if (len(files) == 0):
            print("[!] Not Found!")
            return

        userSelect = fzf.prompt(files)

        if userSelect:
            userSelect = userSelect[0]
            print ("[*] Copying %s --> %s ..." % (userSelect, target))
            os.system("cp '%s' '%s' " % (userSelect,target))
            return
        else:
            print("[!] User cancel select.")