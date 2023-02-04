def Install():
    print("[RedTeamTools] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/A-poc/RedTeam-Tools.git RedTeamTools")

def Uninstall():
    print("[RedTeamTools] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/RedTeamTools")

def Upgrade():
    print("[RedTeamTools] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/RedTeamTools/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))