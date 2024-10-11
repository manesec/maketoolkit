import configparser
import subprocess,os,sys
from pyfzf.pyfzf import FzfPrompt

def listScript():
    nolist = True
    for path,subpaths,files in os.walk("/var/lib/mkt/Script"):
        for file in files:
            if file[-3:] == ".py":
                abs_path = (path + "/"+ file)
                module_name = abs_path[:-3]
                module_name = module_name.replace("/var/lib/mkt/Script/","")
                print("[%s]" %module_name )
                nolist = False

                print("  ",end='')
                from importlib.machinery import SourceFileLoader
                SourceFileLoader("manesec",abs_path).load_module().description()

    if (nolist):
        print("[!] There are no any script can be use.")


def useScript(inputName):
    fzf = FzfPrompt()

    # Query all script, here call module
    all_module = []
    for path,subpaths,files in os.walk("/var/lib/mkt/Script"):
        for file in files:
            if file[-3:] == ".py":
                module_name = (path + "/"+ file)[:-3]
                module_name = module_name.replace("/var/lib/mkt/Script/","")
                all_module.append(module_name)
    all_module.sort()

    if len(all_module) == 0: 
        print("[ERROR] No such script.")
        sys.exit(1)
    
    if inputName:
        # have input value
        matched = []
        for module in all_module:
            if inputName.lower() in module.lower():
                matched.append(module)
        
        if len(matched) == 0:
            print("[!] No such script.")
            sys.exit(1)

        if len(matched) > 1:
            userSelect = fzf.prompt(matched)

            if userSelect:
                userSelect = userSelect[0]
                print ("[*] Selected: %s" % userSelect)
                from importlib.machinery import SourceFileLoader
                SourceFileLoader("manesec",os.path.abspath("/var/lib/mkt/Script/" + userSelect + ".py")).load_module().Run()            
            else:
                print("[!] User cancel select.")

        elif len(matched) == 1:
            # When have one tools
            from importlib.machinery import SourceFileLoader
            SourceFileLoader("manesec",os.path.abspath("/var/lib/mkt/Script/" + matched[0] + ".py")).load_module().Run()

    else:
        # no input value
        userSelect = fzf.prompt(all_module,"--preview-window follow --preview-window=wrap --preview \"mkt desc script '{}' \"")

        if userSelect:
            userSelect = userSelect[0]
            print ("[*] Selected: %s" % userSelect)
            from importlib.machinery import SourceFileLoader
            SourceFileLoader("manesec",os.path.abspath("/var/lib/mkt/Script/" + userSelect + ".py")).load_module().Run()            
        else:
            print("[!] User cancel select.")

