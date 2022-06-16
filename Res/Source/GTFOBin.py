def Install():
    print("[GTFOBins] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/GTFOBins/GTFOBins.github.io.git GTFOBins")

def Uninstall():
    print("[GTFOBins] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/GTFOBins")

def Upgrade():
    print("[GTFOBins] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/GTFOBins/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))