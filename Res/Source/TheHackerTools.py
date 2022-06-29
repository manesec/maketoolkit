def Install():
    print("[TheHackerTools] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/ShutdownRepo/The-Hacker-Tools.git TheHackerTools")

def Uninstall():
    print("[TheHackerTools] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/TheHackerTools")

def Upgrade():
    print("[TheHackerTools] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/TheHackerTools/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))