def Install():
    print("[BaseDB] Downloading db ...")
    import os
    os.chdir("/var/lib/mkt/Res/Data/")
    os.system("git clone https://github.com/manesec/maketoolkit-db.git BaseDB")
    os.chdir("/var/lib/mkt/Res/Data/BaseDB")
    
    from importlib.machinery import SourceFileLoader
    SourceFileLoader("manesec","/var/lib/mkt/Res/Data/BaseDB/Build.py").load_module().Run()    

def Uninstall():
    print("[BaseDB] Removing db...")
    import os
    os.system("rm -rf /var/lib/mkt/Res/Data/BaseDB")

def Upgrade():
    print("[BaseDB] The BaseDB not support to upgrade, but you can uninstall and install it again.")
    print("Try to run:")
    print("    sudo mkt db uninstall BaseDB")
    print("    sudo mkt db install BaseDB")