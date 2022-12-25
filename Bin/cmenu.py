import os,sys

print("""
         __      __                .__          
  _____ |  | ___/  |_  ____   ____ |  |   ______
 /     \|  |/ /\   __\/  _ \ /  _ \|  |  /  ___/
|  Y Y  \    <  |  | (  <_> |  <_> )  |__\___ \ 
|__|_|  /__|_ \ |__|  \____/ \____/|____/____  >
      \/     \/                              \/ 
                By @manesec
      https://github.com/manesec/maketoolkit""")

# ==========================================================================
#                                Function
# ==========================================================================

def ReturnFalse () : return False

def PrintLine():
    print("-"*50)

# ==========================================================================
#                                  Menu
# ==========================================================================

def FirstMenu() -> bool:
    while True: 
        PrintLine()

        print(""" Please select your function :) 

    [T] Tools Manager.
    [D] Search DB Manager.
    [S] Running Script.
    [U] Update the mkt tools.
    
    [Q] Exit.
        """)

        GetUserInput = input(" # mkt :").strip().lower()

        if GetUserInput == "q":
            print("bye! by manesec.")
            sys.exit(0)
        
        SelectFunction = {
            "u" : SecondMKTUpdate,
            "s" : SecondScript,
            # todo
        }

    
        if SelectFunction.get(GetUserInput,ReturnFalse)() : break

def SecondDB() -> bool:

    return False


def SecondScript() -> bool:
    while True:
        PrintLine()
        print(""" What script you want to run?
        """)

        ScriptList = []

        nolist = True
        for path,subpaths,files in os.walk("/var/lib/mkt/Script"):
            for file in files:
                if file[-3:] == ".py":
                    module_name = (path + "/"+ file)[:-3]
                    module_name = module_name.replace("/var/lib/mkt/Script/","")
                    ScriptList.append(module_name)
                    nolist = False
        if (nolist):
            print("        [*] There are no any script can be use.")
            return False

        # List all script
        index = 0
        for script in ScriptList:
            print("    [%s] %s" % (index,script))
            index += 1

        print("\n    [B] Back.\n")

        GetUserInput = input(" # mkt script :").strip().lower()

        if (GetUserInput == "b"):
            return False

        if (GetUserInput.isdigit()):
            if (int(GetUserInput) >= len(ScriptList)) or (int(GetUserInput) < 0):
                print("Out of the list :)")
                continue

            if input("Run # mkt script %s ? [y/n]" % (ScriptList[int(GetUserInput)])).lower() == "y":
                PrintLine()
                os.system("mkt script %s" % (ScriptList[int(GetUserInput)]))


def SecondMKTUpdate() -> bool:
    while True:

        PrintLine()
        print(""" Are you sure to update ?

    All tools will be DELETED !!!
    Cause need to update the source.

        [Y]es    [N]o
        """)

        GetUserInput = input(" # mkt update :").strip().lower()
        if (GetUserInput == "y"):
            print("Running #mkt update ...")
            PrintLine()
            os.system("mkt update")
            sys.exit(0)
        return False

# ==========================================================================
#                                  Main
# ==========================================================================

print("TODO!")

if __name__ == "__main__" :    
    if (os.getuid() != 0):
        print("[Err] Please run as root !")
        sys.exit(0)
    FirstMenu()
