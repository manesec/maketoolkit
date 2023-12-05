def Install():
    print("[AmsiBypassPowershell] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell.git AmsiBypassPowershell")

def Uninstall():
    print("[AmsiBypassPowershell] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/AmsiBypassPowershell")

def Upgrade():
    print("[AmsiBypassPowershell] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/AmsiBypassPowershell/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))