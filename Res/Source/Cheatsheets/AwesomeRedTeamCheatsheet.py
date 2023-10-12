def Install():
    print("[AwesomeRedTeamCheatsheet] Downloading db ...")
    import os
    # mkdir
    from pathlib import Path
    absSavePath = "/var/lib/mkt/Res/Data/Cheatsheets/"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone https://github.com/RistBS/Awesome-RedTeam-Cheatsheet.git AwesomeRedTeamCheatsheet")

def Uninstall():
    print("[AwesomeRedTeamCheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Cheatsheets/AwesomeRedTeamCheatsheet")

def Upgrade():
    print("[AwesomeRedTeamCheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Cheatsheets/AwesomeRedTeamCheatsheet/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))