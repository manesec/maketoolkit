def Install():
    print("[XapaxSecurity] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/xapax/security.git XapaxSecurity")

def Uninstall():
    print("[XapaxSecurity] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/XapaxSecurity")

def Upgrade():
    print("[XapaxSecurity] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/XapaxSecurity/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))