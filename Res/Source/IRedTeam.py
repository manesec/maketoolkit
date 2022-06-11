def Install():
    print("[IRedTeam] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques.git IRedTeam")
    os.system("rm -rf /var/lib/mkt/Res/Data/IRedTeam/lab")

def Uninstall():
    print("[IRedTeam] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/IRedTeam")

def Upgrade():
    print("[IRedTeam] The IRedTeam not support to upgrade, but you can uninstall and install it again.")
    print("Try to run:")
    print("    sudo mkt db uninstall IRedTeam")
    print("    sudo mkt db install IRedTeam")