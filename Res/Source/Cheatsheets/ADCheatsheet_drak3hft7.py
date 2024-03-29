
def Install():
    print("[ADCheatsheet] Downloading db ...")

    import os
    # mkdir
    from pathlib import Path
    absSavePath = "/var/lib/mkt/Res/Data/Cheatsheets/"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone https://github.com/drak3hft7/Cheat-Sheet---Active-Directory ADCheatSheet_drak3hft7")

def Uninstall():
    print("[ADCheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Cheatsheets/ADCheatSheet_drak3hft7")

def Upgrade():
    print("[ADCheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Cheatsheets/ADCheatSheet_drak3hft7/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))