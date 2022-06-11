def Install():
    print("[ADCheatsheet] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/S1ckB0y1337/Active-Directory-Exploitation-Cheat-Sheet.git ADCheatsheet_S1ckB0y1337")

def Uninstall():
    print("[ADCheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/ADCheatsheet_S1ckB0y1337")

def Upgrade():
    print("[ADCheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/ADCheatsheet_S1ckB0y1337/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))