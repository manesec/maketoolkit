#! /bin/bash

# This is pre-setup env script.

echo [Step 1] Apt update ...
apt update

echo [Step 2] Apt Installing ....
apt install -y unzip python3 python3-pip wget less pipx

echo [Step 3] Setuping pip ...
pip3 install --upgrade pip
pip3 install requests

echo [Step 4] Install MKT ...
python3 install.py

echo [Step 5] Run mkt command ...
mkt 

echo [Step Final] Running the test ...
python3 -u buildallfortest.py
