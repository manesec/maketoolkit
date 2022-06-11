def Install():
    print("[PayloadsAllTheThings] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git PayloadAllTheThings")

def Uninstall():
    print("[PayloadsAllTheThings] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/PayloadAllTheThings")

def Upgrade():
    print("[PayloadsAllTheThings] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/PayloadAllTheThings/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))