def Info():
    print("    This script will install all the DB.")

def Run():
    import os
    print("[InstallAllDB] Running ...")
    for dirpath,_,filenames in os.walk("/var/lib/mkt/Res/Source"):
        for file in filenames:
            dbName = (dirpath + "/" +file)
            dbName = dbName.replace("/var/lib/mkt/Res/Source/","")
            dbName = (dbName[:-3])
            os.system("mkt db install %s" % (dbName))