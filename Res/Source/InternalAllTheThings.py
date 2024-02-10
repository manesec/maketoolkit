def Install():
    print("[InternalAllTheThings] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/swisskyrepo/InternalAllTheThings.git InternalAllTheThings")

def Uninstall():
    print("[InternalAllTheThings] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/InternalAllTheThings")

def Upgrade():
    print("[InternalAllTheThings] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/InternalAllTheThings/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))