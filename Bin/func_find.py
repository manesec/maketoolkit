import configparser
import subprocess,os
from pyfzf.pyfzf import FzfPrompt

def findinFiles(filename):
    config = configparser.ConfigParser()
    config.read('/etc/mkt.conf')
    default_shell = (config['Mkt']['ShellProgram']).strip()
    fzf = FzfPrompt()

    if (filename[0] == None):
        command = "find /Tools/ -type f -not -name '*\.mkt' -not -path '*/.git/*' " 
        status,output_str = subprocess.getstatusoutput(command)
        files = output_str.split('\n')

        if (len(files) == 0):
            print("[!] Not such files, please install some tools.")
            return

        userSelect = fzf.prompt(files,"--preview-window=wrap --preview \"cat '{}' \"")
        if userSelect:
            userSelect = userSelect[0]
            print ("[*] Selected: %s" % userSelect)
            os.chdir(os.path.dirname(userSelect))
            os.system(default_shell)
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
            print("[!] Not Found!")
            return

        userSelect = fzf.prompt(files,"--preview-window=wrap --preview \"cat '{}' \"")

        if userSelect:
            userSelect = userSelect[0]
            print ("[*] Selected: %s" % userSelect)
            os.chdir(os.path.dirname(userSelect))
            os.system(default_shell)
            return
        else:
            print("[!] User cancel select.")