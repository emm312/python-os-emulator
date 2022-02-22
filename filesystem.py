class File:
    def __init__(self, name, ext, parentFolder):
        self.name = name
        self.ext = ext
        self.parentFolder = ""
    def getParentFolder(self):
        return self.parentFolder
    #make a ToJson method
    def toJson(self):
        return {
            "name": self.name,
            "ext": self.ext
        }


class Folder:
    def __init__(self, name, parentFolder):
        self.name = name
        self.parentFolder = parentFolder
        self.files = []
        self.folders = []
    # make a addFolder and addFile method
    def addFile(self, file):
        self.files.append(file)
    def addFolder(self, folder):
        self.folders.append(folder)
    def removeFolder(self, name):
        for folder in self.folders:
            if folder.name == name:
                self.folders.remove(folder)
                return
            else:
                print("Folder not found.")
        
    def removeFile(self, name):
        for file in self.files:
            if file.name == name:
                self.files.remove(file)
                return
            else:
                print("File not found.")
    
    # make a toJson function
    def toJson(self):
        # remember to convert the files and folders to json
        return {self.name : {
            "name": self.name,
            "parentFolder": self.parentFolder,
            "files": [file.toJson() for file in self.files],
            "folders": [folder.toJson() for folder in self.folders]
        }}