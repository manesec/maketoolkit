def Install():
    print("[CRTP-Notes] Downloading db ...")
    import os
    # mkdir
    from pathlib import Path
    absSavePath = "/var/lib/mkt/Res/Data/Notes/"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone https://github.com/0xStarlight/CRTP-Notes.git CRTP_Notes")

def Uninstall():
    print("[CRTP-Notes] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Notes/CRTP_Notes")

def Upgrade():
    print("[CRTP-Notes] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Notes/CRTP_Notes")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))