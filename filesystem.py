class File:
    def __init__(self, name, ext):
        self.name = name
        self.ext = ext


    def getFullName(self):
        return self.name+"."+self.extension
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

    # make a toJson function
    def toJson(self):
        # remember to convert the files and folders to json
        return {name : {
            "name": self.name,
            "parentFolder": self.parentFolder,
            "files": [file.toJson() for file in self.files],
            "folders": [folder.toJson() for folder in self.folders]
        }}