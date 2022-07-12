def Info():
    print("This script will install raccoon-scanner.")

def Run():
    import os
    print("[raccoon-scanner] Running ...")
    os.system("pip3 install raccoon-scanner")
    print("Install done. Example:")
    print("    $ raccoon")