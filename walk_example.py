import glob
import os
import fnmatch

PathStart = '/Users/rduvalwa2/'

def get_directories_path(path):
    directoriesList =   [] 
    filesList = []
    pathNode = glob.glob(os.path.join(path, "*")) # get all files in path
    for file in pathNode:
        if os.path.isfile(file):
            filesList.append(file)
        if os.path.isdir(file):
            directoriesList.append(file)
    return (directoriesList,filesList)

def get_dir_files(path,searchString):
    foundFiles = []
    startDirectories = get_directories_path(path)
    for start in startDirectories[0]:
            if os.path.isdir(start):
                for root, dir, files in os.walk(start):
                    for item in  files:
                        if item.endswith(searchString):
                            foundFile = root + "/" + item
                            foundFiles.append(foundFile)
    return  foundFiles

if __name__ == '__main__':
    PathStart = '/Users/rduvalwa2/DevTools/eclipse-luna/workspace/OReilly_Python/'
    
#    result = get_directories_path(PathStart)
#    print(result[0])
#    print(result[1])
#    get_dir_files(PathStart, ".py")
    PathStart = '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Sir Douglas Quintet/'
    f = get_dir_files(PathStart, ".m4a")

    for item in f:
        print(item)
    print(len(f))    