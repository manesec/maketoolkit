def Install():
    print("[ARTToolkit] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/arttoolkit/arttoolkit.github.io.git ARTToolkit")

def Uninstall():
    print("[ARTToolkit] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/ARTToolkit")

def Upgrade():
    print("[ARTToolkit] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/ARTToolkit/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))