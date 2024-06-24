import configparser
import subprocess,os,sys
from pyfzf.pyfzf import FzfPrompt
import shutil

from importlib.machinery import SourceFileLoader
Unit = SourceFileLoader("manesec","/var/lib/mkt/Bin/module_unit.py").load_module()

isDebug = False

def Debug(mess):
    """ simple Debug Options """
    if isDebug:
        print(mess)


def Parser_Tools_String_When_Install(inputString):
    fzf = FzfPrompt()

    # pre-load the tools list
    toolsList = []
    for path,subpaths,files in os.walk("/var/lib/mkt/Tools/Source/"):
        for file in files:
            if file[-4:] == ".mkt":
                module_name = (path + "/"+ file)[:-4]
                module_name = module_name.replace("/var/lib/mkt/Tools/Source/","")
                toolsList.append(module_name)
    Debug("toolsList => " + str(toolsList))

    # input file detect
    find_mkt = False
    abs_file = None
    relative_file = None

    if inputString :
        # add if not extension
        input_str = inputString.strip()
        if (len(input_str)<=4) or (input_str[-4:] != ".mkt"):
            input_str += ".mkt"

        # fix bug for deleted folder path
        systempwd = "/tmp"
        try:
            if (os.path.isabs(input_str)):
                systempwd = os.path.abspath(input_str)
            else:
                systempwd = os.getcwd() + "/" + input_str
                systempwd = os.path.abspath(systempwd)
        except: pass

        if (os.path.exists("/var/lib/mkt/Tools/Source/" + input_str)):
            Debug("Detected Method => 1")
            abs_file = "/var/lib/mkt/Tools/Source/" + input_str
            relative_file = input_str
            find_mkt = True

        if (systempwd.startswith("/var/lib/mkt/Tools/Source/") and (find_mkt == False)):
            if ((os.path.exists(systempwd))):
                Debug("Detected Method => 2")
                abs_file = systempwd
                relative_file = systempwd.replace("/var/lib/mkt/Tools/Source/","")
                find_mkt = True

        if (systempwd.startswith("/Tools/") and (find_mkt == False)):
            if ((os.path.exists(systempwd))):
                Debug("Detected Method => 3")
                abs_file = systempwd
                relative_file = systempwd.replace("/Tools/","")
                find_mkt = True

        # Find in tools list
        if (find_mkt == False):
            Debug("Detected Method => 4")
            finded_Tools = []
            for tools in toolsList:
                if (input_str[:-4].lower() in tools.lower()):
                    Debug("Hit => " + tools)
                    finded_Tools.append(tools)

            if (len(finded_Tools) > 1):
                # When more than one tools
                Debug(finded_Tools)

                userSelect = fzf.prompt(finded_Tools)

                if userSelect:
                    userSelect = userSelect[0]
                    print ("[*] Selected: %s" % userSelect)
                    abs_file = "/var/lib/mkt/Tools/Source/" + userSelect + ".mkt"
                    relative_file = userSelect
                    find_mkt = True
                    
                else:
                    print("[!] User cancel select.")
                    sys.exit(1)

            elif (len(finded_Tools) == 1):
                # When have one tools
                Debug("Return => " + finded_Tools[0])
                abs_file = "/var/lib/mkt/Tools/Source/" + finded_Tools[0] + ".mkt"
                relative_file = finded_Tools[0]
                find_mkt = True
    else:
        # user select 
        Debug("Input None, fall back to Select mode")
        userSelect = fzf.prompt(toolsList)

        if userSelect:
            userSelect = userSelect[0]
            print ("[*] Selected: %s" % userSelect)
            abs_file = "/var/lib/mkt/Tools/Source/" + userSelect + ".mkt"
            relative_file = userSelect
            find_mkt = True
            
        else:
            print("[!] User cancel select.")
            sys.exit(1)

    if (find_mkt == False):
        print("[ERROR] Can not find the tools, No such file.")
        sys.exit(1)

    relative_path = None
    if (abs_file.startswith("/var/lib/mkt/Tools/Source/")):
        relative_file = os.path.basename(abs_file)
        relative_path = os.path.dirname(abs_file).replace("/var/lib/mkt/Tools/Source/","")
    elif (abs_file.startswith("/Tools/")):
        relative_file = os.path.basename(abs_file)
        relative_path = os.path.dirname(abs_file).replace("/Tools/","")
    else:
        print("[ERROR] The mkt file path without standard paths.")
        sys.exit(1)
    if (os.path.exists("/var/lib/mkt/Tools/Install/" + relative_path + "/" + relative_file)):
        print("[ERROR] %s already installed." % (relative_path + "/" + relative_file.replace(".mkt","")))
        sys.exit(1)

    if not (os.path.exists(abs_file)):
        print("[ERROR] Can not find the tools, No such file.")
        sys.exit(1)

    Debug("relative_path => " + relative_path)
    Debug("relative_file => " + relative_file)
    Debug("abs_file => " + abs_file)

    return relative_path,relative_file,abs_file

def Parser_Tools_String_When_Uninstall(inputString):
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
        # add .mkt
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
        # user select 
        Debug("Input None, fall back to Select mode")
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



def install(inputString):
    Unit.CheckUID()
    relative_path, relative_file, abs_file = Parser_Tools_String_When_Install(inputString)

    from pathlib import Path
    path = Path("/var/lib/mkt/Tools/Install/" + relative_path)
    path.mkdir(parents=True, exist_ok=True)
    shutil.move(abs_file,"/var/lib/mkt/Tools/Install/" + relative_path + "/" + relative_file)

    from importlib.machinery import SourceFileLoader
    SourceFileLoader("manesec","/var/lib/mkt/Tools/Install/" + relative_path + "/" +relative_file).load_module().Install()
    Unit.CleanUp()

def uninstall(inputString):

    Unit.CheckUID()
    abs_file,module_name = Parser_Tools_String_When_Uninstall(inputString)

    shutil.move(abs_file,"/var/lib/mkt/Tools/Source/" + module_name)

    from importlib.machinery import SourceFileLoader
    SourceFileLoader("manesec","/var/lib/mkt/Tools/Source/" + module_name).load_module().Uninstall()

    Unit.CleanUp()

def reinstall(inputString):
    Unit.CheckUID()
    abs_file,module_name = Parser_Tools_String_When_Uninstall(inputString)

    cwd = os.getcwd()
    from importlib.machinery import SourceFileLoader
    SourceFileLoader("manesec",abs_file).load_module().Uninstall()
    os.chdir(cwd)
    SourceFileLoader("manesec",abs_file).load_module().Install()

    Unit.CleanUp()

def upgrade(inputString):
    Unit.CheckUID()
    abs_file,module_name = Parser_Tools_String_When_Uninstall(inputString)

    from importlib.machinery import SourceFileLoader
    SourceFileLoader("manesec",abs_file).load_module().Upgrade()

    Unit.CleanUp()

def upgradeAll():
    Unit.CheckUID()
    print("[*] Upgrade all the tools ...")
    nolist = True
    for path,subpaths,files in os.walk("/var/lib/mkt/Tools/Install/"):
        for file in files:
            if file[-4:] == ".mkt":
                abs_path = (path + "/"+ file)
                module_name = abs_path[:-4]
                module_name = module_name.replace("/var/lib/mkt/Tools/Install/","")
                print("[*] Pre-running %s ..." %module_name )
                nolist = False

                from importlib.machinery import SourceFileLoader
                SourceFileLoader("manesec",abs_path).load_module().Upgrade()
    if (nolist):
        print("[!] There are no tools installed.")
    Unit.CleanUp()