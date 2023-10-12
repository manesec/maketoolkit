def Install():
    print("[BugBountyCheatSheet] Downloading db ...")
    import os
    # mkdir
    from pathlib import Path
    absSavePath = "/var/lib/mkt/Res/Data/Cheatsheets/"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone https://github.com/EdOverflow/bugbounty-cheatsheet.git BugBountyCheatSheet")

def Uninstall():
    print("[BugBountyCheatSheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Cheatsheets/BugBountyCheatSheet")

def Upgrade():
    print("[BugBountyCheatSheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Cheatsheets/BugBountyCheatSheet/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))