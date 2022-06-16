def Install():
    print("[LOLBAS] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/LOLBAS-Project/LOLBAS.git LOLBAS")

def Uninstall():
    print("[LOLBAS] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/LOLBAS")

def Upgrade():
    print("[LOLBAS] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/LOLBAS/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))