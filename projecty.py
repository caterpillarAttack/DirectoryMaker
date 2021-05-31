#!/usr/bin/python3
import os
import sys

# Run the script with an space after specifying the name of a project.
# Add another space after that argument should you want multiple projects to be created.
# (Single Project Example)
# project.py ProjectName1
# (Multiple Project Example)
# project.py ProjectName1 ProjectName2 ProjectName3

applicationDict = {
"SecondLife" : ["Textures", "Scripts", "Sounds", "Animations", "Models"],
"QuixelMixer" : ["SecondLife", "Blender"],
"SubstancePainter" : ["Textures", "Models"],
"SubstanceDesigner" : ["Resources"],
"Photoshop" : ["1K" , "2K", "4K", "8K"],
"Blender" : ["Models", "Textures"],
"Marmoset" : ["Models", "Textures"],
"GameReady" : ["SecondLife", "Unreal", "Unity"],
# "Example" : ["test\textures", "somethingElse", ]
}


class DirectoryMaker:
    users = []
    projDir = ""
    createDirs = []
    def __init__(self, projectName):
        self.projDir = os.getcwd()
        self.baseDir = projectName

    def addDirectory(self, directories):
        # For later expanded functionality.
        if isinstance(directories, str):
            self.createDirs.append(directories)
        elif isinstance(directories, dict):
            for definition in directories.items():
                if len(definition[1]) == 0:
                    self.createDirs.append(definition[0])
                else:
                    self.createDirs += [os.path.join(definition[0], item) for item in definition[1]]
        else:
            raise TypeError("Error, not valid type. Please provide a string or pass in the corresponding application dictionary.")

    def createDirectories(self):
        print("Creating the following directories:")
        for directory in self.createDirs:
            directoryToBeMade  = os.path.join(self.projDir, os.path.join(self.baseDir, directory))
            try:
                os.makedirs(directoryToBeMade)
                print(directoryToBeMade)
            except:
                print('Directory ' + '"' + str(directoryToBeMade) + '"' + " already exists. Skipping.")

    def createToDoList(self):
        tempDir = os.path.join(self.projDir, self.baseDir)
        file = open(os.path.join(tempDir, "todoList_" + str(self.baseDir)+ ".txt"), "a")



# Add Text or XML parser class here to handle larger and more complex projects.




def main():
    if not (len(sys.argv[1:]) >= 1):
        print("Please provide a project name.")
        raise RuntimeError("Please provide at least one project name.")
    else:
        for project in sys.argv[1:]:
            makeDir = DirectoryMaker(project)
            makeDir.addDirectory(applicationDict)
            makeDir.createDirectories()
            makeDir.createToDoList()

if __name__ == "__main__":
    main()
