print("Python OS Loading!")
import os
import filesystem
root_folder = filesystem.Folder("root", None)
fresh_filesys = {"root":{
    "name": "root",
    "parent": None,
    "files": [],
    "folders": [
        {"home" : {
            "name": "home",
            "parent": "root",
            "files": [],
            "folders": []}}]
}}

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
    convertFilesystemToObjects()


def convertFilesystemToObjects():
    for folder in filesys["root"]["folders"]:
        for folder_name in folder:
            folder_obj = filesystem.Folder(folder_name, "root")
            for file in folder[folder_name]["files"]:
                file_obj = filesystem.File(file["name"], file["ext"])
                folder_obj.addFile(file_obj)
            for folder_name in folder[folder_name]["folders"]:
                folder_obj.addFolder(folder_name)
            root_folder.addFolder(folder_obj)
    for file in filesys["root"]["files"]:
        file_obj = filesystem.File(file["name"], file["ext"])
        root_folder.addFile(file_obj)

    
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
        print("mkdir: makes a new folder")
        print("cd: changes directory")
        print("ls: lists files and folders")
        print("rmdir: removes a folder")
        print("rmfile: removes a file")
        print("mkfile: creates a new file")
    elif cmd  == "shutdown":
        break
    elif cmd  == "reset":
        config["isFirstTime"] = 1
        updateConfig()
        filesys = fresh_filesys
        updateFilesystem()
        os.system("python shell.py")
        break
    elif cmd  == "restart":
        updateConfig()
        os.system("python shell.py")
        break
    elif cmd  == "echo":
        try:
            print(userin.split("echo ")[1])
        except:
            print("echo what?")
    elif cmd  == "cls":
        os.system("cls")
    # make me a mkdir command
    elif cmd  == "mkdir":
        updateFilesystem()
            # make a folder with the name of the userin and make the parent folder the currentdir
        currdir.addFolder(filesystem.Folder(userin.split("mkdir ")[1], currdir.name))
        filesys = currdir.toJson()
        updateFilesystem()
    # make me a removedir command
    elif cmd  == "rmdir":
        currdir.removeFolder(userin.split("rmdir ")[1])
        filesys = root_folder.toJson()
        updateFilesystem()

    # make a make file command
    elif cmd  == "mkfile":
        try:
            currdir.addFile(filesystem.File(userin.split("mkfile ")[1], userin.split("mkfile ")[1].split(".")[1]))
            filesys = currdir.toJson()
            updateFilesystem()
        except:
            print("please specify an extension")

    # make a remove file command
    elif cmd  == "rmfile":
        currdir.removeFile(userin.split("rmfile ")[1])
        filesys = root_folder.toJson()
        updateFilesystem()
    # make me a cd command
    elif cmd  == "cd":
        if userin.split("cd ")[1] == "..":
            if currdir.parent != None:
                currdir = currdir.parent
        else:
            try:
                currdir = currdir.folders[userin.split("cd ")[1]]
            except:
                print("folder does not exist")
    elif cmd == "":
        pass
    else:
        print("Invalid command.")
    
            

print("Python os has shut down")