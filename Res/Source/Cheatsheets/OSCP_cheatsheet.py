
def Install():
    print("[OSCP_cheatsheet] Downloading db ...")
    import os
    # mkdir
    from pathlib import Path
    absSavePath = "/var/lib/mkt/Res/Data/Cheatsheets/"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone https://github.com/0xJs/OSCP_cheatsheet OSCP_cheatsheet")

def Uninstall():
    print("[OSCP_cheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Cheatsheets/OSCP_cheatsheet")

def Upgrade():
    print("[OSCP_cheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Cheatsheets/OSCP_cheatsheet/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))
