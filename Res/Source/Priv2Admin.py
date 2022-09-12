def Install():
    print("[Priv2Admin] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/gtworek/Priv2Admin.git Priv2Admin")

def Uninstall():
    print("[Priv2Admin] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Priv2Admin")

def Upgrade():
    print("[Priv2Admin] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Priv2Admin/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))