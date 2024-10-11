def description():
    print("This script will install Name that hash(NTH).")

def Run():
    import os
    os.system("pip3 install name-that-hash")
    print("Install done. Example:")
    print("    $ nth -t <hash>")