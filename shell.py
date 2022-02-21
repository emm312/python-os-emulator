print("Python OS Loading!")
import os
import filesystem
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
    elif cmd.split()[0] == "shutdown":
        break
    elif cmd.split()[0] == "reset":
        config["isFirstTime"] = 1
        updateConfig()
        os.system("python shell.py")
        break
    elif cmd.split()[0] == "restart":
        updateConfig()
        os.system("python shell.py")
        break
    elif cmd.split()[0] == "echo":
        try:
            print(userin.split("echo ")[1])
        except:
            print("echo what?")
    elif cmd.split()[0] == "cls":
        os.system("cls")
    # make me a mkdir command
    elif cmd.split()[0] == "mkdir":
        try:
            name = userin.split("mkdir ")[1]
            newFolder = filesystem.Folder(name, currdir.name)
            config = root_folder.addFolder(newFolder)

            updateFilesystem()
        except:
            pass

    # make me a cd command
    elif cmd.split()[0] == "cd":
        try:
            name = userin.split("cd ")[1]
            currdir = currdir[name]
        except:
            if userin.split("cd ")[1] == "..":
                currdir = currdir.parentFolder
            else:
                print("Invalid command.")
    elif cmd == "":
        pass
    else:
        print("Invalid command.")
    
            

print("Python os has shut down")