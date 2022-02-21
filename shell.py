print("Python OS Loading!")
import os
import filesystem
import hashlib
root_folder = filesystem.Folder("root", None)
fresh_filesys = {
    "name": "root",
    "parent": None,
    "files": [],
    "folders": [
        {"home" : {
            "name": "home",
            "parent": "root",
            "files": [],
            "folders": []}}]
}
try:
    import json

except:
    os.system("pip install json")
    import json



with open('config.json', 'r') as outfile:
    
    config = json.load(outfile)
def updateConfig():
    with open('config.json', 'w') as out:
        json.dump(config, out)
updateConfig()


with open('filesystem.json', 'r') as outfile:
    filesys = json.load(outfile)

def updateFilesystem():
    with open('filesystem.json', 'w') as out:
        json.dump(filesys, out, indent=4)



isOn = True
print("Done!")


if config["isFirstTime"] == 1:
    config["isFirstTime"] = 0
    config["username"] = input("What is your username> ")
    updateConfig()


currdir = root_folder

while True:
    userin = input(f"pythonOS@{config['username']}:{currdir.name}> ")
    commands = userin.split(" ")
    cmd = commands[0]
    if cmd == "help":
        print("help: shows this!")
        print("echo: Says what you say after the command")
        print("reset: resets system to factory settings")
        print("shutdown: turns off os")
        print("reboot: reboots the os")
        print("cls: clears screen")
    elif cmd.startswith("shutdown"):
        break
    elif cmd.startswith("reset"):
        config["isFirstTime"] = 1
        updateConfig()
        os.system("python shell.py")
        break
    elif cmd.startswith("restart"):
        updateConfig()
        os.system("python shell.py")
        break
    elif cmd.startswith("echo"):
        try:
            print(userin.split("echo ")[1])
        except:
            pass
    elif cmd.startswith("cls"):
        os.system("cls")
    # make me a mkdir command
    elif cmd.startswith("mkdir"):
        try:
            name = userin.split("mkdir ")[1]
            newFolder = filesystem.Folder(name, currdir.name)
            config = root_folder.addFolder(newFolder)

            updateFilesystem()
        except:
            pass

    # make me a cd command
    elif cmd.startswith("cd"):
        try:
            name = userin.split("cd ")[1]
            currdir = root_folder.cd(name)
        except:
            if userin.split("cd ")[1] == "..":
                currdir = root_folder.cd("..")
            else:
                print("Invalid command.")
    else:
        print("Invalid command.")
    
            

print("Python os has shut down")