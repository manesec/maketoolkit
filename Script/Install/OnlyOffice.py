from importlib.machinery import SourceFileLoader
Unit = SourceFileLoader("manesec_github","/var/lib/mkt/Bin/module_unit.py").load_module()

def Info():
    print("This script will install OnlyOffice.")

def Run():
    import os
    Download_link = "https://download.onlyoffice.com/install/desktop/editors/linux/onlyoffice-desktopeditors_amd64.deb"
    Unit.WgetDownloadFile(Download_link, "/tmp/onlyoffice-desktopeditors_amd64.deb")
    os.system("apt install -y fonts-crosextra-carlito")
    os.system("dpkg -i onlyoffice-desktopeditors_amd64.deb")
    os.system("rm /tmp/onlyoffice-desktopeditors_amd64.deb")