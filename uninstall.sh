#! /bin/bash

# check sudo
if [ "$(id -u)" != "0" ]; then
    echo "ERROR: Please run as root user."
    exit 1
fi

echo "Uninstalling mkt ..."
unlink /bin/mkt
unlink /bin/mkt-update
unlink /Tools

rm -rf /var/lib/mkt/