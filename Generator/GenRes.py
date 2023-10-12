#! /bin/bash
# This file used to generator a res base on git clone only.

# Input File format
# Git link || branches || name
inputfile = "input.list"
absSavePath = "/var/lib/mkt/Res/Data/Cheatsheets/"

from pathlib import Path
import os
os.mkdir('output')

def genconfig(git,branch,name):
    savefiles = """
def Install():
    print("[{name}] Downloading db ...")
    import os
    # mkdir
    from pathlib import Path
    absSavePath = "{abspath}"
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)    

    os.chdir(absSavePath)
    os.system("git clone {git} {name}")

def Uninstall():
    print("[{name}] Removing db...")
    import os
    os.system("rm -rf {abspath}{name}")

def Upgrade():
    print("[{name}] Checking and upgrading ...")
    import os
    os.chdir("{abspath}{name}/")
    Branches = "{branch}"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))
""".format(name=name,branch=branch,abspath=absSavePath,git=git)

    savefile = open("output/" + name + ".py",'w',encoding='utf-8')
    savefile.writelines(savefiles)
    savefile.close()

with open(inputfile,'r',encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line == "" : continue
        linelist = line.split("||")
        genconfig(linelist[0].strip(),linelist[1].strip(),linelist[2].strip())
