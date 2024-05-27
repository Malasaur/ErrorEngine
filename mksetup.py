"""
ERRENG -> C:\Users\Public\
startup.bat -> C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

@echo off
C:\Users\Public\ERRENG\wpy\python-3.12.3.amd64 C:\Users\Public\ERRENG\erreng.pyw
"""
import os, sys, json

drive = sys.argv[1][0].upper()+":"
ID = sys.argv[2]
public = os.path.join(drive, "Users", "Public")
erreng = os.path.join(public, "ERRENG")
errengExc = os.path.join(erreng, "erreng.pyw")
python = os.path.join(erreng, "wpy", "python-3.12.3.amd64")
pythonExc = os.path.join(python, "python.exe")
startup = os.path.join(drive, "ProgramData", "Microsoft", "Windows", "Start Menu", "Programs", "StartUp")
dataJson = os.path.join("ERRENG", "data.json")

startupData = f"""@echo off
"{pythonExc}" "{errengExc}" 
"""

setupData = f"""@echo off
copy "ERRENG" "{public}" 
copy "startup.bat" "{startup}"
"""

jsonData = {
    "ID": ID,
    "requirements": ["gitpython"]
}

open("startup.bat", "w").write(startupData)
open("setup.bat", "w").write(setupData)
json.dump(jsonData, open(dataJson, "w"))
