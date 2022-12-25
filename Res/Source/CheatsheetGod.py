def Install():
    print("[CheatsheetGod] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/OlivierLaflamme/Cheatsheet-God.git CheatsheetGod")

def Uninstall():
    print("[CheatsheetGod] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/CheatsheetGod")

def Upgrade():
    print("[CheatsheetGod] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/CheatsheetGod/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))