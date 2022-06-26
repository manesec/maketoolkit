def Info():
    print("    This script will install Name that hash(NTH).")

def Run():
    import os
    print("[Name that hash] Running ...")
    os.system("pip3 install name-that-hash")
    print("Install done. Example:")
    print("    $ nth -t <hash>")