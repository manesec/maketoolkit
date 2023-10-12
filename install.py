#! /bin/python3

import os,sys,shutil

if (os.getuid() != 0):
    print("ERROR: Please run as root user.")
    sys.exit(1)

# Step 1 - Checking Command
requests_command = ["less","git","wget","unzip"]

for check_command in requests_command:
    runcode = os.WEXITSTATUS(os.system("command -v %s > /dev/null" % (check_command)))
    if (runcode != 0):
        print("ERROR: %s not found on your system." % (check_command))
        sys.exit(1)

# Step 2 - Install Library
os.system("pip3 install -r requirements.txt")

# Step 3 - Copying the base
if (os.path.exists("/etc/mkt.conf")):
    os.remove("/etc/mkt.conf")
shutil.copy("mkt.conf","/etc/mkt.conf")

if (os.path.exists("/var/lib/mkt")):
    os.system("rm -rf /var/lib/mkt")
os.system("mkdir -p /var/lib/mkt")
os.system("cp -r . /var/lib/mkt")

# Setp 4 - Setup the env
os.system("chmod -R 755 /var/lib/mkt/")
os.system("ln -s /var/lib/mkt/Tools/Source /Tools")
os.system("ln -s /var/lib/mkt/mkt /bin/mkt")
os.system("ln -s /var/lib/mkt/mkt-update /bin/mkt-update")

os.system("mkdir -p /var/lib/mkt/Res/Data")
os.system("mkdir -p /var/lib/mkt/Res/Install")
os.system("mkdir -p /var/lib/mkt/Tools/Install")
os.system("mkdir -p /var/lib/mkt/Tools/Version")

print("""OK!

========================  Note  ========================
All the tools will be install in /var/lib/mkt/Tools/Source/
Config will be in /etc/mkt.conf
Soft link will be create: /var/lib/mkt/Tools/Source/ -->  /Tools
========================================================
""")