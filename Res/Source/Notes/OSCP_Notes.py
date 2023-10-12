def Install():
    print("[OSCP-Notes] Downloading db ...")
    import os
    # mkdir
    from pathlib import Path
    absSavePath = "/var/lib/mkt/Res/Data/Notes/"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone https://github.com/AidenPearce369/OSCP-Notes.git OSCP_Notes")

def Uninstall():
    print("[OSCP-Notes] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Notes/OSCP_Notes")

def Upgrade():
    print("[OSCP-Notes] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Notes/OSCP_Notes")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))