def Install():
    print("[HackTricks] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/carlospolop/hacktricks.git HackTricks")

def Uninstall():
    print("[HackTricks] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/HackTricks")

def Upgrade():
    print("[HackTricks] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/HackTricks/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))