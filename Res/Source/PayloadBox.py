def Install():
    print("[PayloadBox] Downloading db ...")


    from pathlib import Path
    path = Path("/var/lib/mkt/Res/Data/PayloadBox")
    path.mkdir(parents=True, exist_ok=True)
    
    import os
    os.chdir("/var/lib/mkt/Res/Data/PayloadBox")


    os.system("git clone https://github.com/payloadbox/command-injection-payload-list.git command-injection-payload-list")
    os.system("git clone https://github.com/payloadbox/ssti-payloads.git ssti-payloads")
    os.system("git clone https://github.com/payloadbox/xss-payload-list.git xss-payload-list")
    os.system("git clone https://github.com/payloadbox/sql-injection-payload-list.git sql-injection-payload-list.git")
    os.system("git clone https://github.com/payloadbox/rfi-lfi-payload-list.git rfi-lfi-payload-list")
    os.system("git clone https://github.com/payloadbox/csv-injection-payloads.git csv-injection-payloads")
    os.system("git clone https://github.com/payloadbox/directory-payload-list.git directory-payload-list")
    os.system("git clone https://github.com/payloadbox/open-redirect-payload-list.git open-redirect-payload-list")
    os.system("git clone https://github.com/payloadbox/xxe-injection-payload-list.git  xxe-injection-payload-list")

def Uninstall():
    print("[PayloadBox] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/PayloadBox")

def Upgrade():
    print("[PayloadBox] Checking and upgrading ...")
    import os
    folderList = ["command-injection-payload-list", "ssti-payloads", "xss-payload-list", "sql-injection-payload-list.git",
        "rfi-lfi-payload-list", "csv-injection-payloads", "directory-payload-list", "open-redirect-payload-list",
        "xxe-injection-payload-list"]

    for f in folderList:
        os.chdir("/var/lib/mkt/Res/Data/PayloadBox/%s" % f)
        Branches = "master"
        os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))



