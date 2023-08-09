def Install():
    print("[Handbooks] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/0xsyr0/Awesome-Cybersecurity-Handbooks.git Handbooks")

def Uninstall():
    print("[Handbooks] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Handbooks")

def Upgrade():
    print("[Handbooks] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/Handbooks/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))