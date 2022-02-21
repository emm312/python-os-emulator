print("Emms OS Loading!")

import os
import filesystem
root_folder = filesystem.Folder("root", None)
try:
    import json

except:
    os.system("pip install json")
    import json

with open('config.json', 'r') as outfile:
    config = json.load(outfile)

with open('filesystem.json', 'r') as outfile:
    filesys = json.load(outfile)


isOn = True
print("Done!")
def updateConfig():
    with open('config.json', 'w') as out:
        json.dump(config, out)
updateConfig()
def updateFilesystem():
    filesys = root_folder.toJson()
    with open('filesystem.json', 'w') as out:
        json.dump(filesys, out)

if config["isFirstTime"] == 1:
    config["isFirstTime"] = 0
    config["username"] = input("What is your username> ")
    updateConfig()


student = filesystem.Folder("e", None)
json_data = json.dumps(student.__dict__)
print(json_data)



while True:
    userin = input(config["username"] + " Home $ ")
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
            config = root_folder.addFolder(name)

            updateFilesystem()
        except:
            pass
    else:
        print("Invalid command.")

print("manali os has shut down sad")