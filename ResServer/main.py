import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,PlainTextResponse,FileResponse
import os,subprocess
import json
import configparser
config = configparser.ConfigParser()
config.read('/etc/mkt.conf')

doc_location = "/var/lib/mkt/Res/Data"

app = FastAPI()

app.mount("/html", StaticFiles(directory="html"), name="html")

@app.get("/",response_class=RedirectResponse)
def redirectHome():
    return RedirectResponse("html/files.html")

def replace_space(value):
    reserved_chars = r'''?&!{}()^~*:\\"'+-'''
    for ch in reserved_chars:
        value = value.replace(ch,"")
    return value

# List dir
@app.get("/api/dir")
def listdir(q:str):
    return_object = {"message":"Unknow Error", "code":"-1"}
    try:
        query_folder = os.path.abspath(doc_location + "/" + q)
        if not (query_folder.startswith(doc_location)):
            return_object["code"] = "-1"    
            return_object["message"] = "Access Denied"    
            return return_object 

        if not os.path.exists(query_folder):
            return_object["code"] = "-1"    
            return_object["message"] = "File Not found"    
            return return_object 

        Dir_List = []
        for obj in os.listdir(query_folder):
            if (os.path.isdir(query_folder + "/" + obj)):
                Dir_List.append([obj,"D"])
            else:
                Dir_List.append([obj,"F"])
            
        Dir_List.sort()
        return_object["result"] = Dir_List
        return_object["code"] = "0"    
        return return_object
    except:
        return return_object

# Search
@app.get("/api/search")
def search(q:str):
    if (q):
        result = subprocess.getoutput("python3 /var/lib/mkt/Bin/api_search.py search '" + replace_space(q) + "'")
        if result.strip() == "" :
            return {"result":result}

        result = json.loads(result)
        return {"result":result}


# Read files
@app.get("/api/read",response_class=PlainTextResponse)
def getfile(q:str):
    try:
        query_file = os.path.abspath(doc_location + "/" + q)
        if not (query_file.startswith(doc_location)):
            return "Access Denied."

        if not os.path.exists(query_file):
            return "File no exists."

        file = open(query_file, "r")
        return PlainTextResponse(file.read())
    except Exception as err:
        return "File can no be preview. Please see the raw files."

# Read files
@app.get("/api/download",response_class=PlainTextResponse)
def getfile(q:str):
    try:
        query_file = os.path.abspath(doc_location + "/" + q)
        if not (query_file.startswith(doc_location)):
            return "Access Denied."

        if not os.path.exists(query_file):
            return "File no exists."

        if (os.path.isdir(query_file)):
            return "File no exists."
        return FileResponse(query_file)
    except:
        return "Unable to open the file"

if __name__ == "__main__":
    uvicorn.run(app, host=config['DocServer']["ListenAddr"], port=int(config['DocServer']["ListenPort"]))