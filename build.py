import sys, os, shutil

file = sys.argv[1]

def wpython(args):
    os.system(r'wine "/home/malasaur/.wine/drive_c/Program Files/Python312/python.exe" ' + args)

wpython("-m PyInstaller "+file+" --onefile --noconsole")

efile = file.split(".")[0]+".exe"
os.rename("dist/"+efile, efile)
shutil.rmtree("dist")
shutil.rmtree("build")
os.remove(efile.split(".")[0]+".spec")