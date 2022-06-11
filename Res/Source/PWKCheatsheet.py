def Install():
    print("[PWKCheatsheet] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/ibr2/pwk-cheatsheet.git PWKCheatsheet")

def Uninstall():
    print("[PWKCheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/PWKCheatsheet")

def Upgrade():
    print("[PWKCheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/PWKCheatsheet/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))