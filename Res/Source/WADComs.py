def Install():
    print("[WADComs] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/WADComs/WADComs.github.io.git WADComs")

def Uninstall():
    print("[WADComs] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/WADComs")

def Upgrade():
    print("[WADComs] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/WADComs/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))