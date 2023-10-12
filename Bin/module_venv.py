import os

def getVenvPath(venv_name):
    from pathlib import Path
    return str(Path.home()) + "/mkt/" + venv_name

def active(venv_name):
    current_path = os.getcwd()

    if (os.path.exists(getVenvPath(venv_name))):
        os.chdir(getVenvPath(venv_name))
        command = "bash -c 'source bin/activate; bash; exit '" 
        os.system(command)
    else:
        print("[ERROR] venv not found.")

    os.chdir(current_path)

def activeRunCommand(venv_name,command):
    # using base64 to carry the bash
    import base64
    enc = base64.b64encode(command.encode('utf-8'))
    b64 = enc.decode('utf-8')

    # run command
    current_path = os.getcwd()
    if (os.path.exists(getVenvPath(venv_name))):
        os.chdir(getVenvPath(venv_name))
        command = "bash -c 'source bin/activate; echo \"%s\" | base64 -d | bash; exit '" % (b64)
        os.system(command)

    os.chdir(current_path)

def remove(venv_name):
    from pathlib import Path
    target_path = str(Path.home()) + "/mkt/" + venv_name
    if (os.path.exists(target_path)):
        print("[*] Deleting " + target_path + " ...")
        os.system("rm -rf " + target_path)

    if (os.path.exists(target_path)):
        print("[WARN] Seem to be delete failed, running as sudo ...")
        os.system("sudo rm -rf " + target_path)

def create(venv_name):
    from pathlib import Path
    target_path = str(Path.home()) + "/mkt/" 
    path = Path(target_path)
    path.mkdir(exist_ok=True,parents=True)

    current_path = os.getcwd()
    os.chdir(target_path)
    os.system("python3 -m venv " + venv_name)
    os.chdir(current_path)

