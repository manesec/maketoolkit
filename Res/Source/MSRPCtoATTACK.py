def Install():
    print("[MSRPCtoATTACK] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/jsecurity101/MSRPC-to-ATTACK.git MSRPCtoATTACK")

def Uninstall():
    print("[MSRPCtoATTACK] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/MSRPCtoATTACK")

def Upgrade():
    print("[MSRPCtoATTACK] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/MSRPCtoATTACK/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))