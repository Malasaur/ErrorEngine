"""
Find Windows partition
    List partitions
    For each partition check if it has the "Windows" folder
Setup ERRENG folder
    Create "C:\\Windows\\Users\\Public"
    Copy erreng.py and WinPython to the folder
Setup autostart
    Run schtasks through cmd.exe with Wine
    Set the PC to execute winpython erreng.py as admin on boot
Exit
"""

import subprocess, os, json

"""
    process = await asyncio.create_subprocess_exec(
        os.path.join("ERRENG", executable),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if stdout:
        log(f"{executable} stdout:\n{stdout.decode()}")
    if stderr:
        log(f"{executable} stderr:\n{stderr.decode()}")
"""

def exec(*args):
    proc = subprocess.Popen(
        *args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = proc.communicate()
    return stdout.decode(), stderr.decode()

def get_partitions(main=True, sub=False):
    parts = []
    out = exec("lsblk")[0].split("\n")[1:]
    for part in out:
        if not part:
            continue
        if part[0] in "qwertyuiopasdfghjklzxcvbnm":
            if not main:
                continue
        else:
            if not sub:
                continue
            part = part[2:]
        data = part.split()
        parts.append(("/dev/"+data[0], data[3]))
    return parts

def mount(dir):
    exec("sudo", "mount", dir, "/mnt")

def umount():
    exec("sudo umount /mnt")

def find_windows(confirm=False):
    for part, size in get_partitions(False, True):
        if confirm:
            if (input("Mount "+part+"? ")+" ")[0].lower() != "y":
                continue
        mount(part)
        if "Windows" in os.listdir("/mnt"):
            umount()
            return part
        umount()
    return "NULL" #None

def makedir(dir):
    exec("sudo", "mkdir", "/mnt/Users/Public/"+dir)

def copy(file, r=False, dest="ERRENG"):
    exec("sudo", "cp", file, "/mnt/Users/Public/"+dest+(" -r" if r else ""))

def schtask(name, *args):
    #schtasks /create /tn "YourTaskName" /tr "C:\path\to\your\file.exe argument1 argument2" /sc onlogon /rl highest /f
    exec(
        "wine",
        "/mnt/Windows/System32/schtasks.exe",
        "/create",
        "/tn",
        name,
        "/tr",
        '"'+' '.join(args)+'"', 
        "/sc",
        "onlogon",
        "/rl",
        "highest",
        "/f"
    )

def log(msg, lvl=0):
    print("  "*lvl+"[i]", msg)

def ask(msg, lvl=0):
    return input(" "*lvl+"[?]"+msg)

def main():
    log("Looking for Windows...")
    win = find_windows()
    mount(win)
    log("Windows found in "+win)

    log("Setting up ERRENG folder")
    makedir("ERRENG")
    copy("erreng.pyw")
    copy("WinPython", True)
    ID = ask("Enter an ID for this instance: ", 1)
    json.dump({"ID": ID, "data": {}}, open("/mnt/Users/Public/ERRENG/data.json", "w"))
    log("ERRENG folder setup")

    log("Scheduling the Engine...")
    schtask(
        "ErrorEngine", 
        "C:\\Users\\Public\\ERRENG\\WinPython\\python-3.12.3.amd64\\python.exe C:\\Users\\Public\\ERRENG\\erreng.pyw"
    )
    log("erreng.py scheduled")

    input(" :] Done! Press enter to shutdown the PC: ")
    umount()
    exec("shutdown now")

if __name__ == "__main__":
    main()