def Info():
    print("This script will be install all search DB.")

def Run():
    import os
    for dirpath,_,filenames in os.walk("/var/lib/mkt/Res/Source"):
        for file in filenames:
            dbName = (dirpath + "/" +file)
            dbName = dbName.replace("/var/lib/mkt/Res/Source/","")
            dbName = (dbName[:-3])
            os.system("mkt db install %s" % (dbName))