def Install():
    print("[AtomicRedTeam] Downloading db ...")

    import os,shutil

    from pathlib import Path
    path = Path("/tmp/mktools")
    path.mkdir(exist_ok=True,parents=True)
    path = Path("/var/lib/mkt/Res/Data/AtomicRedTeam")
    path.mkdir(exist_ok=True,parents=True)    
    
    os.chdir("/tmp/mktools")
    os.system("git clone https://github.com/redcanaryco/atomic-red-team.git AtomicRedTeam")

    os.chdir("/tmp/mktools/AtomicRedTeam/atomics")
    
    for path,_,files in os.walk("/tmp/mktools/AtomicRedTeam/atomics"):
        for file in files:
            if (file[-2:] == "md"):
                shutil.copy(path + "/" + file,"/var/lib/mkt/Res/Data/AtomicRedTeam/")
    os.chdir("/tmp")
    os.system("rm -rf /tmp/mktools")

def Uninstall():
    print("[AtomicRedTeam] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/AtomicRedTeam")

def Upgrade():
    print("[AtomicRedTeam] The AtomicRedTeam not support to upgrade, but you can uninstall and install it again.")
    print("Try to run:")
    print("    sudo mkt db uninstall AtomicRedTeam")
    print("    sudo mkt db install AtomicRedTeam")