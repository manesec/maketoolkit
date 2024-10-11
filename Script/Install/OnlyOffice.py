from importlib.machinery import SourceFileLoader
Unit = SourceFileLoader("manesec_github","/var/lib/mkt/Bin/module_unit.py").load_module()

def description():
    print("This script will install OnlyOffice.")

def Run():
    from importlib.machinery import SourceFileLoader
    SourceFileLoader("require_root","/var/lib/mkt/Bin/module_unit.py").load_module().RequireRoot()

    import os
    Download_link = "https://download.onlyoffice.com/install/desktop/editors/linux/onlyoffice-desktopeditors_amd64.deb"
    Unit.WgetDownloadFile(Download_link, "/tmp/onlyoffice-desktopeditors_amd64.deb")
    os.system("apt install -y fonts-crosextra-carlito")
    os.system("dpkg -i /tmp/onlyoffice-desktopeditors_amd64.deb")
    os.system("rm /tmp/onlyoffice-desktopeditors_amd64.deb")
    print("OK")