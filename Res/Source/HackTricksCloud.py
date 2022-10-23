def Install():
    print("[HackTricksCloud] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/carlospolop/hacktricks-cloud.git HackTricksCloud")

def Uninstall():
    print("[HackTricksCloud] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/HackTricksCloud")

def Upgrade():
    print("[HackTricksCloud] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/HackTricksCloud/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))