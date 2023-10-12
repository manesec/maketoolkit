def Install():
    print("[RedTeamingTacticsandTechniques] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques.git RedTeamingTacticsandTechniques")
    os.system("rm -rf /var/lib/mkt/Res/Data/RedTeamingTacticsandTechniques/lab")

def Uninstall():
    print("[RedTeamingTacticsandTechniques] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/RedTeamingTacticsandTechniques")

def Upgrade():
    print("[RedTeamingTacticsandTechniques] The RedTeamingTacticsandTechniques not support to upgrade, but you can uninstall and install it again.")
    print("Try to run:")
    print("    sudo mkt db uninstall RedTeamingTacticsandTechniques")
    print("    sudo mkt db install RedTeamingTacticsandTechniques")

    