def Install():
    print("[AwesomeCybersecurityHandbooks] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/0xsyr0/Awesome-Cybersecurity-Handbooks.git AwesomeCybersecurityHandbooks")

def Uninstall():
    print("[AwesomeCybersecurityHandbooks] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/AwesomeCybersecurityHandbooks")

def Upgrade():
    print("[AwesomeCybersecurityHandbooks] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/AwesomeCybersecurityHandbooks/")
    Branches = "main"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))