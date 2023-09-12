def Install():
    print("[BugBountyCheatSheet] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/EdOverflow/bugbounty-cheatsheet.git BugBountyCheatSheet")

def Uninstall():
    print("[BugBountyCheatSheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/BugBountyCheatSheet")

def Upgrade():
    print("[BugBountyCheatSheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/BugBountyCheatSheet/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))