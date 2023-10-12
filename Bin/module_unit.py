def WgetDownloadFile(url,local_path,quiet = False):
    import os

    if os.path.exists(local_path + ".tmp"):
        os.remove(local_path)

    if os.path.exists(local_path):
        os.remove(local_path)

    quiet = "--quiet" if quiet else ""
    os.system('wget "%s" %s -O "%s"' % (url,quiet,local_path + ".tmp"))
    os.rename(local_path + ".tmp", local_path)

def RollBack(module_name):
    import os
    os.chdir("/var/lib/mkt")
    os.system("mkt remove " + module_name)


def DebPackageSuggestInstall(pkgName):
    import apt,os
    cache = apt.Cache()
    try:
        if cache[pkgName].is_installed:
            pass
        else:
            print("[*] Trying to using apt to install: %s " % (pkgName))
            os.system("sudo apt install -y %s" % (pkgName))
    except:
        print("[WARNING] %s no found in your system packages, maybe your system unsupported" % (pkgName) )
