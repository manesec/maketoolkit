def Install():
    print("[AwesomeRedTeamCheatsheet] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/RistBS/Awesome-RedTeam-Cheatsheet.git AwesomeRedTeamCheatsheet")

def Uninstall():
    print("[AwesomeRedTeamCheatsheet] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/AwesomeRedTeamCheatsheet")

def Upgrade():
    print("[AwesomeRedTeamCheatsheet] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/AwesomeRedTeamCheatsheet/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))