def Install():
    print("[PenetrationTestingGrimoire] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/RackunSec/Penetration-Testing-Grimoire.git PenetrationTestingGrimoire")

def Uninstall():
    print("[PenetrationTestingGrimoire] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/PenetrationTestingGrimoire")

def Upgrade():
    print("[PenetrationTestingGrimoire] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/PenetrationTestingGrimoire/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))