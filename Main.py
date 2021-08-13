import os

Package = input("Package:")
FPackage = "cmd/c " + '"python -m pip install ' + Package + '"'
print("Installing:" + FPackage)

#Input Path to Python.exe
os.chdir('Put Path here')
os.system(FPackage)
os.system('cls')
