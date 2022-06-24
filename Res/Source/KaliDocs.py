def Install():
    print("[KaliDocs] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://gitlab.com/kalilinux/documentation/kali-docs.git KaliDocs")

def Uninstall():
    print("[KaliDocs] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/KaliDocs")

def Upgrade():
    print("[KaliDocs] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/KaliDocs/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))