def Info():
    print("This script will install Netexec.")

def Run():
    import os
    os.system("sudo apt install pipx git")
    os.system("pipx ensurepath")
    os.system("pipx install git+https://github.com/Pennyw0rth/NetExec")
    print("Install done. Example:")
    print("    $ netexec")