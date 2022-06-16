def Install():
    import os
    print("[Mimikatz] Downloading db ...")

    absSavePath = "/var/lib/mkt/Res/Data/Tools/"
    from pathlib import Path
    path = Path(os.path.dirname(absSavePath))
    path.mkdir(parents=True, exist_ok=True)
    
    os.chdir(absSavePath)
    os.system("git clone https://github.com/gentilkiwi/mimikatz.wiki.git Mimikatz")

def Uninstall():
    print("[Mimikatz] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/Tools/Mimikatz")

def Upgrade():
    print("[Mimikatz] Not support upgrade, but you can uninstall and install it again.")