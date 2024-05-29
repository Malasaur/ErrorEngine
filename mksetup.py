import os, sys, json

drive = sys.argv[1][0].upper()+":"+"\\"
ID = sys.argv[2]
"""
public = drive+os.path.join("Users", "Public")
cpublic = "C:\\"+os.path.join("Users", "Public")
erreng = os.path.join(public, "ERRENG")
cerreng = os.path.join(cpublic, "ERRENG")
errengExc = os.path.join(erreng, "erreng.pyw")
cerrengExc = os.path.join(cerreng, "erreng.pyw")
python = os.path.join(erreng, "wpy", "python-3.12.3.amd64")
cpython = os.path.join(cerreng, "wpy", "python-3.12.3.amd64")
pythonExc = os.path.join(python, "python.exe")
cpythonExc = os.path.join(cpython, "python.exe")
startup = drive+os.path.join("ProgramData", "Microsoft", "Windows", "Start Menu", "Programs", "StartUp")
cstartup = "C:\\"+os.path.join("ProgramData", "Microsoft", "Windows", "Start Menu", "Programs", "StartUp")
dataJson = os.path.join("ERRENG", "data.json")
"""

erreng = drive+os.path.join("Users", "Public", "ERRENG")
scripts = "C:\\"+os.path.join("Users", "Public", "ERRENG", "wpy", "python-3.12.3.amd64", "Scripts")
startup = drive+os.path.join("ProgramData", "Microsoft", "Windows", "Start Menu", "Programs", "StartUp")
dataJson = os.path.join("ERRENG", "data.json")
setx = drive+os.path.join("Windows", "System32", "setx.exe")

setupData = f"""@echo off
mkdir "{erreng}"
xcopy /E "ERRENG" "{erreng}" 
copy "startup.vbs" "{startup}" 
{setx} PATH "%PATH%;{scripts}"
"""

jsonData = {
    "ID": ID,
    "requirements": ["requests"]
}

open("setup.bat", "w").write(setupData)
json.dump(jsonData, open(dataJson, "w"))
