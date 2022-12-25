def Install():
    print("[HackNote] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/johnsaigle/hack-notes.git HackNote")

def Uninstall():
    print("[HackNote] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/HackNote")

def Upgrade():
    print("[HackNote] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/HackNote/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))