#! /bin/bash

# check sudo
if [ "$(id -u)" != "0" ]; then
    echo "ERROR: Please run as root user."
    exit 1
fi

echo "Uninstalling mkt ..."
unlink /Tools

rm -rf /bin/mkt
rm -rf /bin/mkt-update
rm -rf /var/lib/mkt/