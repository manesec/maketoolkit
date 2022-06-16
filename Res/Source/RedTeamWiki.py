def Install():
    print("[RedTeamWiki] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/redteamwiki/redteamwiki.git RedTeamWiki")

def Uninstall():
    print("[RedTeamWiki] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/RedTeamWiki")

def Upgrade():
    print("[RedTeamWiki] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/RedTeamWiki/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))