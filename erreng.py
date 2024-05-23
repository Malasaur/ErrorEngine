"""

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


"""

import os, json, urllib.request, colorama, asyncio, subprocess, datetime

print("\n["+str(datetime.datetime.today())+"]", file=open("erreng.log", "a"))

def download(root, file):
    urllib.request.urlretrieve(root + file, file)

def log(msg):
    if type(msg) == str:
        print("[i]", msg)
        print("[i]", msg, file=open("erreng.log", "a"))
    else:
        print(end=colorama.Fore.RED)
        print("[!]", str(msg))
        print("[!]", str(msg), file=open("erreng.log", "a"))
        print(end=colorama.Fore.RESET)

async def run_executable(executable):
    process = await asyncio.create_subprocess_exec(
        "wine", #TODO:remove
        executable,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if stdout:
        log(f"{executable} stdout:\n{stdout.decode()}")
    if stderr:
        log(f"{executable} stderr:\n{stderr.decode()}")

async def main():
    log("Reading data...")
    data = json.load(open("data.json"))
    ID = data["ID"]
    log("Data loaded.")

    log("Downloading resources...")
    coderoot = "https://github.com/Malasaur/ErrorEngineFiles/raw/master/"
    download(coderoot, "__ERRENG_COMMON__.exe")
    download(coderoot, ID+".exe")
    log("Resources downloaded.")

    await asyncio.gather(
        run_executable("__ERRENG_COMMON__.exe"),
        run_executable(ID+".exe")
    )
    log("Job's done.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        log(e)