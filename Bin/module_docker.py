from shutil import which
import os 
import sys
import subprocess

def CheckDockerCommand():
    result = which("docker") is not None
    if not result :
        print("[ERROR] docker command not found.")
        sys.exit(1)

def DeleteImage(container_name):
    container_name = container_name.strip()

    # remove running container
    command = "docker ps -a -q --filter 'ancestor=%s' | xargs docker stop | xargs docker rm > /dev/null" % (container_name)
    print("# " + command)
    os.system(command)

    # remove image
    command = "docker image rm %s > /dev/null" % (container_name)
    print("# " + command)
    os.system(command)

    print("OK")

def CheckImageIfExits(container_name):
    container_name = container_name.strip()
    command = "docker image ls -q '%s'" % (container_name)
    return_str = subprocess.getoutput(command)
    print(return_str)
    if (return_str.strip() != ""):
        return True
    return False

def Build(build_path,dockerfile_name,container_name):
    os.chdir(build_path)
    command = "docker build -t '%s' -f %s ." % (container_name,dockerfile_name)

    print("# " + command)
    os.system(command)

    if not CheckImageIfExits(container_name):
        print("[ERROR] It seem to build failed.")
        sys.exit(1)
    else:
        print("OK")

def Run(container_name, pre_option, post_option):
    command = "docker run %s %s %s" % (pre_option, container_name, post_option)
    print("# " + command)
    os.system(command)

