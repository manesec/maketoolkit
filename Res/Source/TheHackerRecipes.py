def Install():
    print("[TheHackerRecipes] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/ShutdownRepo/The-Hacker-Recipes.git TheHackerRecipes")

def Uninstall():
    print("[TheHackerRecipes] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/TheHackerRecipes")

def Upgrade():
    print("[TheHackerRecipes] Checking and upgrading ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/TheHackerRecipes/")
    Branches = "master"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))