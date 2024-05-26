import os, shutil

file = "setup.py"

def wpython(args):
    os.system('wine "/home/malasaur/.wine/drive_c/Program Files/Python312/python.exe" ' + args + ' --paths="C:\\Program Files\\Python312\\Lib\\site-packages"')

wpython("-m PyInstaller "+file+" --onefile")

efile = file.split(".")[0]+".exe"
os.rename("dist/"+efile, efile)
shutil.rmtree("dist")
shutil.rmtree("build")
os.remove(efile.split(".")[0]+".spec")
