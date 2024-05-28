import os, subprocess, json, logging, sys, asyncio, zipfile, shutil, io

# Make sure the program is running under the ERRENG folder
os.chdir("C:\\Users\\Public\\ERRENG")

# Global variables
REPO = "https://github.com/Malasaur/ErrorEngineFiles"
PATH = os.path.join("wpy", "python-3.12.3.amd64")
PY = os.path.join(PATH, "python.exe")
data = json.load(open("data.json"))
ID = data["ID"]
coreRequire = data["requirements"]

def pipInstall(*packages): # Used to install python packages
    proc = subprocess.Popen(
        ([PY, "-m"] if os.name=="nt" else [])+[
            "pip", "install",
            *packages
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = map(lambda x: x.decode(), proc.communicate())
    return stdout, stderr

def pipCheck(*packages): # Used to get which packages are not installed
    proc = subprocess.Popen(
        ([PY, "-m"] if os.name=="nt" else [])+[
            "pip", "list"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = map(lambda x: x.decode(), proc.communicate())
    stdout = stdout.lower()
    ret = []
    for pack in packages:
        if pack not in stdout:
            ret.append(pack)
    return ret, stderr

async def runProgram(prog): # Used to asyncronously run a program
    proc = subprocess.Popen(
        ([PY] if os.name=="nt" else ["python"])+[
            os.path.join("Files", prog)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = map(lambda x: x.decode(), proc.communicate())
    await asyncio.sleep(1)
    return stdout, stderr

def download(): # Used to download the ErrEngFiles repo
    r = requests.get("https://github.com/Malasaur/ErrorEngineFiles/archive/refs/heads/master.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(os.getcwd())
    os.rename("ErrorEngineFiles-master", "Files")

# Functions used for logging
def log(*msg):
    logging.info(*msg)
def warning(*msg):
    logging.warning(*msg)
def error(*msg, e=True):
    logging.error(*msg)
    if e:
        sys.exit()
def critical(*msg):
    logging.critical(*msg, exc_info=True)

# Configure logging
logging.basicConfig(
    filename="erreng.log", filemode="a",
    level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
)

async def runner(): # Function that runs the programs
    # Run programs
    [out1, err1], [out2, err2] = await asyncio.gather(
        runProgram("__ERRENG_COMMON__.py"),
        runProgram(ID+".py")
    )
    return out1, out2, err1, err2

try:
    log("---------- Program executed ----------")

    # Install required core packages
    log("Checking for core packages...")
    pcks, err = pipCheck(*coreRequire)
    if err:
        error("Error occured check:\n%s", err)
    if pcks:
        log("Found %d missing package(s). Installing...", len(pcks))
        out, err = pipInstall(*pcks)
        if err:
            error("Error occured during installation:\n%s", err)
        log("Package(s) installed successfully.")
    else:
        log("No packages missing.")

    # Import the core packages
    log("Importing core packages...")
    import requests
    log("Packages imported.")
    
    # Download ErrEngFiles
    log("Downloading Files repo...")
    if os.path.isdir("Files"):
        log("Deleting old repo...")
        shutil.rmtree("Files")
    download()
    log("Repo updated.")

    # Download repo requirements
    log("Reading program requirements...")
    filesRequire = open(os.path.join("Files", "requirements.txt")).read().split("\n")
    log("Requirements loaded successfully.")
    log("Checking for repo packages...")
    pcks, err = pipCheck(*filesRequire)
    if err:
        error("Error occured check:\n%s", err)
    if pcks:
        log("Found %d missing package(s). Installing...", len(pcks))
        out, err = pipInstall(*pcks)
        if err:
            error("Error occured during installation:\n%s", err)
        log("Package(s) installed successfully.")
    else:
        log("No repo packages missing.")

    # Run programs
    log("Everything is ready! Running programs...")
    out1, out2, err1, err2 = asyncio.run(runner())
    if err1:
        error("Common program faulted:\n%s", err1, e=False)
    elif out1:
        print(end=out1)

    if err2:
        error("Specific program faulted:\n%s", err2, e=False)
    elif out2:
        print(end=out2)
        
    log("Job's done.")
    
except:
    critical("Critical error occured:")
