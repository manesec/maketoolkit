def description():
    print("This script will install raccoon-scanner.")

def Run():
    import os
    os.system("pip3 install raccoon-scanner")
    print("Install done. Example:")
    print("    $ raccoon")