def Info():
    print("This script will install Powerview Python.")

def Run():
    import os
    os.system("sudo apt install libkrb5-dev")
    os.system("pip3 install powerview")
    print("Install done. Example:")
    print("    $ powerview")