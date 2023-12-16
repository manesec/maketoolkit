def Install():
    print("[HackingTheCloud] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/Hacking-the-Cloud/hackingthe.cloud.git HackingTheCloud")

def Uninstall():
    print("[HackingTheCloud] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/HackingTheCloud")

def Upgrade():
    print("[HackingTheCloud] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/HackingTheCloud/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))