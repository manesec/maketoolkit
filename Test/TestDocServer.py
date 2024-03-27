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

print("[Test] Document Server: OK")
