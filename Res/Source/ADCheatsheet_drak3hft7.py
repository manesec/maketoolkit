def Install():
    print("[cheatsheet] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/drak3hft7/Cheat-Sheet---Active-Directory ADCheatSheet_drak3hft7")

def Uninstall():
    print("[cheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/ADCheatSheet_drak3hft7")

def Upgrade():
    print("[cheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/ADCheatSheet_drak3hft7/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))