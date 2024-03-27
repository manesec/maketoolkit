def Install():
    print("[NetExecWiki] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/Pennyw0rth/NetExec-Wiki.git NetExecWiki")

def Uninstall():
    print("[NetExecWiki] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/NetExecWiki")

def Upgrade():
    print("[NetExecWiki] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/NetExecWiki/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))