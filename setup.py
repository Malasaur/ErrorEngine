import os, colorama, json, shutil

colorama.just_fix_windows_console()

def log(msg):
    print("[i]", msg)

def warn(msg):
    print(colorama.Fore.YELLOW+"[!]", msg, colorama.Fore.RESET)

def error(msg):
    code = str(sum(ord(c) for c in msg))
    print(colorama.Fore.RED+"[X]", msg, "[CODE: 0x"+"0"*(5-len(code))+code+"]", colorama.Fore.RESET)

def ask(msg):
    return str(input(colorama.Fore.BLUE+"[?] "+msg+colorama.Fore.RESET))

def done(msg):
    print(colorama.Fore.LIGHTGREEN_EX+"[✓]", msg, colorama.Fore.RESET)

# Ask for drive letter and find startup folder
drive = ask("Enter drive letter: ")[0].upper()
dest = drive+":\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"

# Find main program
log("Checking for main program...")
erreng = "erreng.py"
if os.path.isfile(erreng):
    log("Main program found.")

    # Copy main program to startup folder
    log("Copying main program to destination...")
    shutil.copyfile(erreng, dest)
    log("Program injected.")

    # Create "ERRENG" folder in startup folder
    log("Creating ERRENG folder...")
    errengdir = os.path.join(dest, "ERRENG")
    os.mkdir(errengdir)
    log("ERRENG folder created.")

    # Ask for ID
    ID = ask("Choose an ID for this instance: ")
    log("Writing data to file...")

    # Save ID in data file
    data = {"ID": ID, "exec_data": {}}
    json.dump(data, open(os.path.join(dest, "data.json"), "w"))
    log("Data written.")

    done("Setup finished.")
else:
    error("Main program not found.")
