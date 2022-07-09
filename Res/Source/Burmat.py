def Install():
    print("[Burmat] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/burmat/burmat.gitbook.io.git Burmat")

def Uninstall():
    print("[Burmat] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Burmat")

def Upgrade():
    print("[Burmat] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Burmat/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))