import os
import json

import filesystem

print("Python OS Loading!")

root_folder = filesystem.Folder("root", None)
fresh_filesys = {
    
        "name": "root",
        "parent": None,
        "files": [],
        "folders": [
            {
                "name": "home",
                "parent": "root",
                "files": [],
                "folders": []
            }
        ]
    }


with open('config.json', 'r') as f:
    global config
    config = json.load(f)

with open('filesystem.json', 'r') as f:
    global filesys
    filesys = json.load(f)

def update_config():
    with open('config.json', 'w') as out:
        json.dump(config, out)

def update_filesystem():
    with open('filesystem.json', 'w') as out:
        json.dump(filesys, out, indent=4)
    convert_filesystem_to_objects()


def convert_filesystem_to_objects():
    global root_folder
    global filesys
    root_folder = filesystem.Folder(filesys["name"], None)
    for folder in filesys["folders"]:
        root_folder.addFolder(filesystem.Folder(folder["name"], root_folder))
    for file in filesys["files"]:
        root_folder.addFile(filesystem.File(file["name"], file["ext"], root_folder))

update_config()
print("Done!")

if config["isFirstTime"] == 1:
    config["isFirstTime"] = 0
    config["username"] = input("What is your username> ")
    update_config()

currdir = root_folder

while True:
    userin = input(f"pythonOS@{config['username']}:{currdir.name}> ")
    commands = userin.split(" ")
    cmd = commands[0]

    match(cmd):
        case "help":
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

        case "shutdown":
            break

        case "reset":
            config["isFirstTime"] = 1
            update_config()
            filesys = fresh_filesys
            update_filesystem()
            os.system("python shell.py")
            break

        case "restart":
            update_config()
            os.system("python shell.py")
            break

        case "echo":
            try:
                for i in range(1, len(commands)):
                    print(commands[i], end=" ")
                print()
            except:
                print("echo what?")

        case "cls":
            os.system("cls")

        # make me a mkdir command
        case "mkdir":
            update_filesystem()
            # make a folder with the name of the userin and make the parent folder the currentdir
            currdir.addFolder(filesystem.Folder(userin.split("mkdir ")[1], currdir.name))
            filesys = currdir.toJson()
            update_filesystem()

        # make me a removedir command
        case "rmdir":
            currdir.removeFolder(userin.split("rmdir ")[1])
            filesys = root_folder.toJson()
            update_filesystem()

        # make a make file command
        case "mkfile": 
            currdir.addFile(filesystem.File(userin.split("mkfile ")[1], userin.split("mkfile ")[1].split(".")[1], currdir.name))
            filesys = root_folder.toJson()
            update_filesystem()

        # make a remove file command
        case "rmfile":
            currdir.removeFile(userin.split("rmfile ")[1])
            filesys = root_folder.toJson()
            update_filesystem()
        
        # make me a cd command
        case "cd":
            if userin.split("cd ")[1] == "..":
                if currdir.parent != None:
                    currdir = currdir.parent
            else:
                try:
                    currdir = currdir.folders[userin.split("cd ")[1]]
                except:
                    print("folder does not exist")
        
        case "":
            pass

        case _:
            print("Invalid command.")

print("Python os has shut down")
