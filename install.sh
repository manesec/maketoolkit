#! /bin/bash

# check sudo
if [ "$(id -u)" != "0" ]; then
    echo "ERROR: Please run as root user."
    exit 1
fi

# check env
command -v python3 > /dev/null
if [ "$?" -ne 0 ]; then
    echo "ERROR: Python3 not found on your system."
    exit
fi

command -v less > /dev/null
if [ "$?" -ne 0 ]; then
    echo "ERROR: less not found on your system."
    exit
fi

command -v git > /dev/null
if [ "$?" -ne 0 ]; then
    echo "ERROR: git not found on your system."
    exit
fi

command -v wget > /dev/null
if [ "$?" -ne 0 ]; then
    echo "ERROR: wget not found on your system."
    exit
fi

command -v unzip > /dev/null
if [ "$?" -ne 0 ]; then
    echo "ERROR: unzip not found on your system."
    exit
fi

echo "Installing mkt ..."
mkdir -p /var/lib/mkt/

cp mkt.conf /etc/mkt.conf
cp mkt /bin/mkt
cp mkt-update /bin/mkt-update

chmod +x /bin/mkt
chmod +x /bin/mkt-update

echo "Installing Source ..."
cp -r Tools /var/lib/mkt/
cp -r Res /var/lib/mkt/
cp -r Script /var/lib/mkt/
cp -r Data /var/lib/mkt/
cp -r Bin /var/lib/mkt/

mkdir -p /var/lib/mkt/Res/Data
mkdir -p /var/lib/mkt/Res/Install
mkdir -p /var/lib/mkt/Tools/Install
mkdir -p /var/lib/mkt/Tools/Version

chmod -R 755 /var/lib/mkt/

ln -s /var/lib/mkt/Tools/Source /Tools
echo "All the tools will be install in /var/lib/mkt/Tools/Source/"
echo "Config will be in /etc/mkt.conf"
echo "Soft link will be create: /var/lib/mkt/Tools/Source/ -->  /Tools"

