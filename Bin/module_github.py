from importlib.machinery import SourceFileLoader
Unit = SourceFileLoader("manesec_github","/var/lib/mkt/Bin/module_unit.py").load_module()

def CheckGithubAPIQuta():
    import json
    import requests
    from datetime import datetime
    import time

    import configparser
    config = configparser.ConfigParser()
    config.read('/etc/mkt.conf')

    Return_json = ""
    if config['Github']["GithubToken"].strip() != "":
        Return_json = requests.get("https://api.github.com/rate_limit",headers={"Authorization":"token %s" % (config['Github']["GithubToken"].strip())}).text
    else:
        Return_json = requests.get("https://api.github.com/rate_limit").text
    Return_json = json.loads(Return_json)
    Remaining = Return_json["rate"]["remaining"]
    Limit = Return_json["rate"]["limit"]
    Reset = (datetime.utcfromtimestamp(Return_json["rate"]["reset"]) - datetime.utcfromtimestamp(time.time())).seconds / 60
    print("[!] Github API: Remaining %s/%s, Reset in %s minutes later." % (Remaining,Limit,round(Reset,2)))

def ReleasesFileGetFromGithubRepo(RepoName,Names):
    import json,re,sys
    import requests

    import configparser
    config = configparser.ConfigParser()
    config.read('/etc/mkt.conf')

    URL = "https://api.github.com/repos/"+RepoName+"/releases/latest"

    print(" *  Searching Github Repo ...")

    Return_list = []
    Return_json = ""

    if config['Github']["GithubToken"].strip() != "":
        Return_json = requests.get(URL,headers={"Authorization":"token %s" % (config['Github']["GithubToken"].strip())}).text
    else:
        Return_json = requests.get(URL).text

    Return_json = json.loads(Return_json)

    for f in Return_json["assets"]:
        for name in Names:
            if (re.search(name,f["name"])):
                print(" +  Found %s " % (f["name"]))
                Return_list.append([f["name"],f["id"],f["updated_at"],f['browser_download_url']])

    if len(Return_list) == 0:
        print("[ERROR] No found on github repo!")
        sys.exit(0)
    return Return_list

def ProjectGetFilesAndUpdate(repoaddr,branches,files):
    import json,os,sys,subprocess
    import requests

    import configparser
    config = configparser.ConfigParser()
    config.read('/etc/mkt.conf')

    api_url = "https://api.github.com/repos/%s/git/trees/%s?recursive=1" % (repoaddr,branches)
    import requests
    Return_json = ""
    if config['Github']["GithubToken"].strip() != "":
        Return_json = requests.get(api_url,headers={"Authorization":"token %s" % (config['Github']["GithubToken"].strip())}).text
    else:
        Return_json = requests.get(api_url).text
    Return_json = json.loads(Return_json)["tree"]
    
    for afile in files:
        RemotePath,LocalPath = afile
        print(" *  Checking %s ..." % RemotePath)
        if os.path.exists(LocalPath):
            LocalPathSha = subprocess.getoutput("git hash-object %s" % (LocalPath))
            RemotePathSha = ""
            for RemoteFileObj in Return_json:
                if (RemoteFileObj["path"].strip() == RemotePath) : 
                    RemotePathSha = RemoteFileObj["sha"]
                    break
            if (RemotePathSha == ""):
                print("[ERR] %s was not found on github repo!" % (RemotePath))
                sys.exit(0)
            if (LocalPathSha == RemotePathSha):
                print(" !  Already up to date.")
                continue
        print(" *  Updating %s ..." % (RemotePath))
        Unit.WgetDownloadFile("https://raw.githubusercontent.com/%s/%s/%s" % (repoaddr,branches,RemotePath),LocalPath,True)
        print(" +  Finish.")
        continue

def UpdateFromGithubReleaseFiles(RepoName,Files,sign_prefix=""):
    import json,re,os
    import requests

    URL = "https://api.github.com/repos/"+RepoName+"/releases/latest"

    import configparser
    config = configparser.ConfigParser()
    config.read('/etc/mkt.conf')

    print(" *  Searching Github Repo ...")
    
    Return_json = ""
    if config['Github']["GithubToken"].strip() != "":
        Return_json = requests.get(URL,headers={"Authorization":"token %s" % (config['Github']["GithubToken"].strip())}).text
    else:
        Return_json = requests.get(URL).text
    Return_json = json.loads(Return_json)

    if 'message' in Return_json:
        print("[Warning] Github return : %s" % (Return_json['message']))

    for filereg,savelink in Files:
        for f in Return_json["assets"]:
            if (re.search(filereg,f["name"])):
                print(" +  Found %s " % (f["name"]))
                sign_file = "/var/lib/mkt/Tools/Version/" + sign_prefix + os.path.basename(savelink) +".gitid"

                if (os.path.exists(savelink)):
                    if (os.path.exists(sign_file)):
                        save_id = open(sign_file,"r")
                        localid = save_id.read().strip()
                        save_id.close()
                        if (localid == str(f["id"])):
                            print(" !  Already up to date")
                            break

                print(" *  Downloading %s ..." % (f["name"]))
                Unit.WgetDownloadFile(f['browser_download_url'],savelink,quiet=False)
                if (os.path.exists(savelink)):
                    save_id = open(sign_file,"w")
                    save_id.write(str(f["id"]))
                    save_id.close()
                break