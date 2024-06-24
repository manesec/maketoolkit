import os,sys
from pyfzf.pyfzf import FzfPrompt

isDebug = False

def Debug(mess):
    """ simple Debug Options """
    if isDebug:
        print(mess)

def Parser_Tools_String_When_Installed(inputString):
    fzf = FzfPrompt()
    abs_file = None
    module_name = None

    # pre-load installed tools
    toolsList = []
    for path,subpaths,files in os.walk("/var/lib/mkt/Tools/Install/"):
        for file in files:
            if file[-4:] == ".mkt":
                module_name = (path + "/"+ file)[:-4]
                module_name = module_name.replace("/var/lib/mkt/Tools/Install/","")
                toolsList.append(module_name)
    Debug("toolsList => " + str(toolsList))

    if inputString:
        input_str = inputString
        if (len(input_str)<=4) or (input_str[-4:] != ".mkt"):
            input_str += ".mkt"


        finded_Tools = []
        for tools in toolsList:
            if (input_str[:-4].lower() in tools.lower()):
                Debug("Hit => " + tools)
                finded_Tools.append(tools)

        if (len(finded_Tools) == 0): 
            print("[ERROR] No found !")
            sys.exit(1)

        if (len(finded_Tools) > 1):
            # When more than one tools
            Debug(finded_Tools)

            userSelect = fzf.prompt(finded_Tools)

            if userSelect:
                userSelect = userSelect[0]
                print ("[*] Selected: %s" % userSelect)
                abs_file = "/var/lib/mkt/Tools/Install/" + userSelect + ".mkt"
                module_name = userSelect + ".mkt"
                
            else:
                print("[!] User cancel select.")
                sys.exit(1)

        elif (len(finded_Tools) == 1):
            # When have one tools
            Debug("Return => " + finded_Tools[0])
            abs_file = "/var/lib/mkt/Tools/Install/" + finded_Tools[0] + ".mkt"
            module_name = finded_Tools[0] + ".mkt"
    
    else:
        userSelect = fzf.prompt(toolsList)

        if userSelect:
            userSelect = userSelect[0]
            print ("[*] Selected: %s" % userSelect)
            abs_file = "/var/lib/mkt/Tools/Install/" + userSelect + ".mkt"
            module_name = userSelect + ".mkt"
            
        else:
            print("[!] User cancel select.")
            sys.exit(1)

    Debug("abs_file =>" + abs_file)
    Debug("module_name =>" + module_name)
    return abs_file, module_name


def findAndGoToToolsDir(toolsName):
    import configparser
    config = configparser.ConfigParser()
    config.read('/etc/mkt.conf')

    default_shell = (config['Mkt']['ShellProgram']).strip()

    # find the tools
    abs_file, _ = Parser_Tools_String_When_Installed(toolsName)
    switch_dir = (abs_file.replace(".mkt","").replace("/var/lib/mkt/Tools/Install","/Tools"))
    if os.path.exists(switch_dir):
        Debug("CD SWITCH 1")
        os.chdir(switch_dir)
        os.system(default_shell)
        return

    print("[ERROR] No such path.")