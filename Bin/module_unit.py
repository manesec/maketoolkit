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