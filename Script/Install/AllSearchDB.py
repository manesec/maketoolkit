
def description():
    desc = r"""Install all the DB"""
    print(desc)


def Run():
    from importlib.machinery import SourceFileLoader
    SourceFileLoader("require_root","/var/lib/mkt/Bin/module_unit.py").load_module().RequireRoot()
    
    # need to rewrite
    import os
    for dirpath,_,filenames in os.walk("/var/lib/mkt/Res/Source"):
        for file in filenames:
            dbName = (dirpath + "/" +file)
            dbName = dbName.replace("/var/lib/mkt/Res/Source/","")
            dbName = (dbName[:-3])
            os.system("mkt db install %s" % (dbName))