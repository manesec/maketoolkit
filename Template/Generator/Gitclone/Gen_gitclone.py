
def generate_py(URL,REPO,NAME) -> str:
    return f"""

def Install():
    print("[{NAME}] Installing base ...")

    import os
    os.chdir("/var/lib/mkt/Tools/Source/Wordlists")
    os.system("git clone {URL} {NAME}")

def Uninstall():
    print("[{NAME}] Uninstalling ...")

    import os
    os.system("rm -rf /var/lib/mkt/Tools/Source/Wordlists/{NAME}")

def Upgrade():
    print("[{NAME}] Upgrading ...")

    import os
    os.chdir("/var/lib/mkt/Tools/Source/Wordlists/{NAME}")
    
    Branches = "{REPO}"
    os.system("git pull origin %s || (git stash drop && git pull origin %s )" % (Branches,Branches))
    """

with open("list",'r') as readfile:
    for line in readfile:
        if (line.strip() == ""):
            continue
        reads = line.split("||")
        url = reads[0].strip()
        repo = reads[1].strip()
        name = reads[2].strip()

        file = open("Out/" + name + ".mkt",'w')
        file.writelines(generate_py(url,repo,name))
        file.close()