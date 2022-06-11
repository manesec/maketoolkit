def Info():
    print("    It will install glow tools include: ")
    print("         glow")

def Run():
    import os
    print("[InstallBasicTools] Running ...")
    Info()
    os.system("pip3 install pwncat-cs")
    os.system("apt update && apt -y install cherrytree python2")