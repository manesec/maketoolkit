def Install():
    print("[PHP Magic hashes] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/spaze/hashes.git PHPMagicHashes")

def Uninstall():
    print("[PHP Magic hashes] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/PHPMagicHashes")

def Upgrade():
    print("[PHP Magic hashes] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/PHPMagicHashes/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))