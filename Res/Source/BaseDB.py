def Install():
    print("[BaseDB] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/manesec/maketoolkit-db.git BaseDB")

def Uninstall():
    print("[cheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/BaseDB")

def Upgrade():
    print("[cheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/BaseDB/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))