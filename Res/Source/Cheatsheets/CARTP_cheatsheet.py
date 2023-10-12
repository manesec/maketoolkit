
def Install():
    print("[CARTP_cheatsheet] Downloading db ...")
    import os
    # mkdir
    from pathlib import Path
    absSavePath = "/var/lib/mkt/Res/Data/Cheatsheets/"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone https://github.com/0xJs/CARTP-cheatsheet CARTP_cheatsheet")

def Uninstall():
    print("[CARTP_cheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Cheatsheets/CARTP_cheatsheet")

def Upgrade():
    print("[CARTP_cheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Cheatsheets/CARTP_cheatsheet/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))
