
def Install():
    print("[CRTE_Cheatsheet] Downloading db ...")
    import os
    # mkdir
    from pathlib import Path
    absSavePath = "/var/lib/mkt/Res/Data/Cheatsheets/"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone https://github.com/0xJs/CRTE-Cheatsheet CRTE_Cheatsheet")

def Uninstall():
    print("[CRTE_Cheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Cheatsheets/CRTE_Cheatsheet")

def Upgrade():
    print("[CRTE_Cheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Cheatsheets/CRTE_Cheatsheet/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))
