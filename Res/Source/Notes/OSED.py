def Install():
    print("[OSED] Downloading db ...")
    import os
    # mkdir
    from pathlib import Path
    absSavePath = "/var/lib/mkt/Res/Data/Notes/"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone https://github.com/nop-tech/OSED.git OSED")

def Uninstall():
    print("[OSED] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Notes/OSED")

def Upgrade():
    print("[OSED] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Notes/OSED")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))