def Install():
    print("[HardwareAllTheThings] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/swisskyrepo/HardwareAllTheThings.git HardwareAllTheThings")

def Uninstall():
    print("[HardwareAllTheThings] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/HardwareAllTheThings")

def Upgrade():
    print("[HardwareAllTheThings] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/HardwareAllTheThings/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))