def Install():
    print("[Ruuand] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/ruuand/ruuand.github.io.git Ruuand")

def Uninstall():
    print("[Ruuand] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Ruuand")

def Upgrade():
    print("[Ruuand] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Ruuand/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))