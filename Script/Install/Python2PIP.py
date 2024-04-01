from importlib.machinery import SourceFileLoader
Unit = SourceFileLoader("manesec_github","/var/lib/mkt/Bin/module_unit.py").load_module()

def Info():
    print("This script will install Python2 Pip.")

def Run():
    import os
    Unit.WgetDownloadFile("https://bootstrap.pypa.io/pip/2.7/get-pip.py","/tmp/get-pip.py")
    os.system("python2 /tmp/get-pip.py")
    os.system("rm -f /tmp/get-pip.py")
    print("OK")