import os, sys, colorama, json

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

if len(sys.argv)-1:
    if sys.argv[1] == "--gui":
        from easygui import *
    else:
        error("Invalid command. Use either `setup` or `setup --gui`.")
else:
    log("Checking for main program...")
    erreng = "erreng.exe"
    dest = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"
    if os.path.isfile(erreng):
        log("Main program found.")
        log("Copying main program to destination...")
        os.system("copy "+erreng+" "+os.path.join(dest))
        log("Program injected.")
        ID = ask("Choose an ID for this instance: ")
        log("Writing data to file...")
        data = {"ID": ID, "exec_data": {}}
        json.dump(data, open(os.path.join(dest, "data.json"), "w"))
        log("Data written.")
        done("Setup finished.")
    else:
        error("Main program not found.")
