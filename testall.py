import os,sys

def CheckUID():
    if os.getuid() != 0 :
        print("[ERROR] Please run as root user.")
        sys.exit()


def CheckDBContent():
    

if __name__ == "__main__" :
    pass