def Install():
    print("[BypassApplocker] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/api0cradle/UltimateAppLockerByPassList.git BypassApplockers")

def Uninstall():
    print("[BypassApplocker] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/BypassApplockers")

def Upgrade():
    print("[BypassApplocker] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/BypassApplockers/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))