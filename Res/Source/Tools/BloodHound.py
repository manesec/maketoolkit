def Install():
    import os
    print("[BloodHound] Downloading db ...")

    absSavePath = "/var/lib/mkt/Res/Data/Tools/"
    from pathlib import Path
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)
    
    os.chdir("/tmp")
    os.system("git clone https://github.com/BloodHoundAD/BloodHound.git BloodHound")
    os.system("mv /tmp/BloodHound/docs /var/lib/mkt/Res/Data/Tools/BloodHound") 
    os.system("rm -rf /var/lib/mkt/Res/Data/Tools/BloodHound/_build")
    os.system("rm -rf /tmp/BloodHound")

def Uninstall():
    print("[BloodHound] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Tools/BloodHound")

def Upgrade():
    print("[BloodHound] Not support upgrade, but you can uninstall and install it again.")