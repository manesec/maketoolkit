import os,sys
def WgetDownloadFile(url,local_path,quiet = False):
    if os.path.exists(local_path + ".tmp"):
        os.remove(local_path)

    if os.path.exists(local_path):
        os.remove(local_path)

    quiet = "--quiet" if quiet else ""
    os.system('wget "%s" %s -O "%s"' % (url,quiet,local_path + ".tmp"))
    os.rename(local_path + ".tmp", local_path)

def RollBack(module_name):
    os.chdir("/var/lib/mkt")
    os.system("mkt remove " + module_name)

def RequireRoot():
    if os.geteuid() != 0:
        print("[ERROR] You need to run this script as root.")
        exit(0)

def CheckUID():
    if os.getuid() != 0 :
        print("[ERROR] Please run as root user.")
        sys.exit(1)

def CleanUp():
    """ delete all `__pycache__` files """
    CheckUID()
    os.system("find /var/lib/mkt/Tools/ -type d -name '__pycache__' | xargs -I $ rm -rf $")
    os.system("chmod -R 755 /var/lib/mkt/")

def extractZipFileAndDelete(zipLocation,fileLists):
    import zipfile,re,shutil

    print("[*] Processing %s ..." % (zipLocation))
    with zipfile.ZipFile(zipLocation, 'r') as zip_ref:
        for zipfilename in zip_ref.namelist():
            for file,location in fileLists:
                dirpath = os.path.dirname(location)
                if (re.search(file,zipfilename)):
                    print("[*] Unzip file %s to %s ..." % (zipfilename,dirpath + "/"))
                    zip_ref.extract(zipfilename, dirpath + "/")
                    if (os.path.abspath(dirpath + "/" + zipfilename) != os.path.abspath(location)):
                        shutil.move(dirpath + "/" + zipfilename, location)
                    break
    os.remove(zipLocation)

def extractGZFileAndDelete(gzLocation,fileLists):
    import tarfile ,re,shutil

    print("[*] Processing %s ..." % (gzLocation))
    with tarfile.open(gzLocation) as f_in:
        for gzfilename in f_in.getnames():
            for file,location in fileLists:
                dirpath = os.path.dirname(location)
                if (re.search(file,gzfilename)):
                    print("[*] Unzip file %s to %s ..." % (gzfilename,dirpath + "/"))
                    f_in.extract(gzfilename, dirpath + "/")
                    if (os.path.abspath(dirpath + "/" + gzfilename) != os.path.abspath(location)):
                        shutil.move(dirpath + "/" + gzfilename, location)
                    break
    os.remove(gzLocation)