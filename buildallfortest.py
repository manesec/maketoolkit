# This is a build for test script.

import os,sys
import time

# Options
TestingDB = False
TestingTools = True
Proxychains = True

RunAsWhileList = True
WhileList = ["Windows/Potato/GodPotato"]
blacklist = ["Tools/xc" , "Tools/Crackmapexec", "Windows/Wesng"]




def Run(command):
    for x in range (1,10):
        code = os.WEXITSTATUS(os.system(command))
        if (code == 0):
            return

        if (code == 1):
            print(f"[Error] Waiting 5 minutes and retrying, {x}/10 ...")
            time.sleep(60*5)
    print("[Error] Found the error, exiting ...")
    sys.exit(1)
    

if TestingDB :
    print("[Step 1] Install all DB for testing ...")

    allDBName = []

    # Collect all db 
    for dirpath,_,filenames in os.walk("/var/lib/mkt/Res/Source"):
        for file in filenames:
            dbName = (dirpath + "/" +file)
            dbName = dbName.replace("/var/lib/mkt/Res/Source/","")
            dbName = (dbName[:-3])
            allDBName.append(dbName)

    print( f"[Step 1] Total DB: {len(allDBName)}")

    for x in range(0,len(allDBName)):
        print(f"[Step 1 - {x + 1}/{len(allDBName)}] Testing DB {allDBName[x]} ...")
        RunCommand = ("mkt db install %s" % (allDBName[x]))
        print("$ " + RunCommand)
        Run(RunCommand)


if TestingTools :
    print("[Step 2] Install all the tools ...")

    allTools = []

    if RunAsWhileList:
        allTools = WhileList
    else:
        for dirpath,_,filenames in os.walk("/var/lib/mkt/Tools/Source"):
            for file in filenames:
                dbName = (dirpath + "/" +file)
                dbName = dbName.replace("/var/lib/mkt/Tools/Source/","")
                dbName = (dbName[:-4])
                
                if (dbName in blacklist):
                    continue
                allTools.append(dbName)

    print( f"[Step 2] Total Tools: {len(allTools)}")

    for x in range(0,len(allTools)):
        print(f"[Step 1 - {x + 1}/{len(allTools)}] Testing Tools {allTools[x]} ...")
        RunCommand = ("mkt install %s" % (allTools[x]))

        time.sleep(60)

        if Proxychains:
            RunCommand = "proxychains " + RunCommand
        print("$ " + RunCommand)
        Run(RunCommand)
