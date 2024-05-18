import os, json, urllib.request, colorama

def download(root, file):
    urllib.request.urlretrieve(root+file, file)

def log(msg):
    print("[i]", msg)

log("Reading data...")
data = json.load(open("data.json"))
ID = data["ID"]
log("Data loaded.")

log("Downloading resources...")
coderoot = "https://github.com/Malasaur/ErrorEngineFiles/raw/master/"
download(coderoot, "__ERRENG_COMMON__.exe")
download(coderoot, ID+".exe")
log("Resources downloaded.")

log("Running common code...")
os.system("__ERRENG_COMMON__.exe")
log("Common executed.")

log("Running local code...")
os.system(ID+".exe")
log("Local code executed.")
