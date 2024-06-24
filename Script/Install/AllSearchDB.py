def Info():
    print("This script will be install all search DB.")

def Run():
    from importlib.machinery import SourceFileLoader
    SourceFileLoader("require_root","/var/lib/mkt/Bin/module_unit.py").load_module().RequireRoot()
    
    import os
    for dirpath,_,filenames in os.walk("/var/lib/mkt/Res/Source"):
        for file in filenames:
            dbName = (dirpath + "/" +file)
            dbName = dbName.replace("/var/lib/mkt/Res/Source/","")
            dbName = (dbName[:-3])
            os.system("mkt db install %s" % (dbName))