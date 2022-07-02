def Info():
    print("This script will be install basic tools include: ")
    print(" - python2, pwncat-cs, cherrytree, glow")

def Run():
    import os
    print("[InstallBasicTools] Running ...")
    Info()
    os.system("pip3 install pwncat-cs")
    os.system("apt update && apt -y install cherrytree python2")
    InstallGlow()


def InstallGlow():
    Files = [
        ["glow_(.){0,}_linux_amd64.deb","/tmp/glow.deb"]
    ]
    UpdateFromGithubReleaseFiles("https://api.github.com/repos/charmbracelet/glow/releases/latest",Files)
    import os
    os.system("dpkg -i /tmp/glow.deb")
    os.system("rm -rf /tmp/glow.deb")

    CheckGithubAPIQuta()

def UpdateFromGithubReleaseFiles(URL,Files):
    import json,re
    import requests

    CONFIG_JSON = json.load(open('/etc/mkt.json','r'))
    print(" *  Searching Github Repo ...")
    
    Return_json = ""
    if CONFIG_JSON["GithubToken"].strip() != "":
        Return_json = requests.get(URL,headers={"Authorization":"token %s" % (CONFIG_JSON["GithubToken"].strip())}).text
    else:
        Return_json = requests.get(URL).text
    Return_json = json.loads(Return_json)

    for filereg,savelink in Files:
        for f in Return_json["assets"]:
            if (re.search(filereg,f["name"])):
                print(" +  Found %s " % (f["name"]))
                print(" *  Downloading %s ..." % (f["name"]))
                WgetDownloadFile(f['browser_download_url'],savelink,quiet=True)

def CheckGithubAPIQuta():
    import json
    import requests
    from datetime import datetime
    import time

    CONFIG_JSON = json.load(open('/etc/mkt.json','r'))

    Return_json = ""
    if CONFIG_JSON["GithubToken"].strip() != "":
        Return_json = requests.get("https://api.github.com/rate_limit",headers={"Authorization":"token %s" % (CONFIG_JSON["GithubToken"].strip())}).text
    else:
        Return_json = requests.get("https://api.github.com/rate_limit").text
    Return_json = json.loads(Return_json)
    Remaining = Return_json["rate"]["remaining"]
    Limit = Return_json["rate"]["limit"]
    Reset = (datetime.utcfromtimestamp(Return_json["rate"]["reset"]) - datetime.utcfromtimestamp(time.time())).seconds / 60
    print("[!] Github API: Remaining %s/%s, Reset in %s minutes later." % (Remaining,Limit,round(Reset,2)))

def WgetDownloadFile(url,local_path,quiet = False):
    import os
    if os.path.exists(local_path):
        os.remove(local_path)
    quiet = "--quiet" if quiet else ""
    os.system('wget "%s" %s -O "%s"' % (url,quiet,local_path))
