import filereadwrite as frw
import htmlparser as parser
import updatedestfile

IDFILENAME = "_idupdated"
CLASSESFILENAME = "__classesupdated"
REMOVEIDFILENAME = "_idremoved"

def updateIds(srcFile,destFolder):
    splitPath = srcFile.split("/")
    srcFilename = splitPath[len(splitPath)-1]
    fileNameSplit = srcFilename.split(".")
    destFileName = destFolder+"/"+fileNameSplit[0] + IDFILENAME + "." + fileNameSplit[1] 
    parser.setIds(frw.readFile(srcFile),destFileName)

def autoCorrectClasses(srcFile,destFile):
    srcIdClassMap = parser.getIdClassMap(frw.readFile(srcFile))
    destSoup = parser.getSoup(frw.readFile(destFile))
    updatedestfile.updateDestFile(srcIdClassMap,destSoup,destFile)

def removeIds(srcFile,destFolder):
    splitPath = srcFile.split("/")
    srcFilename = splitPath[len(splitPath)-1]
    fileNameSplit = srcFilename.split(".")
    destFileName = destFolder+"/"+fileNameSplit[0] + REMOVEIDFILENAME + "." + fileNameSplit[1] 
    parser.removeIds(frw.readFile(srcFile),destFileName)

def doAction(srcFile,destFile,action):
    if action == 1:
        updateIds(srcFile,destFile)
    elif action ==2:
        autoCorrectClasses(srcFile,destFile)
    else:
        removeIds(srcFile,destFile)

    # srcFile = "/home/sham/Desktop/learn/projects/autoupdateclasses/pomato/about_ids_src.html"
    # destFile = "/home/sham/Desktop/learn/projects/autoupdateclasses/pomato/about_ids_dest.html"
    # resultFile = destFile.replace(".html","_classupdated.html")
    # srcContent = frw.readFile(srcFile)
    # destContent = frw.readFile(destFile)
    # srcIdClassMap = parser.getIdClassMap(srcContent)
    # destSoup = parser.getSoup(destContent)
    # updatedestfile.updateDestFile(srcIdClassMap,destSoup,resultFile)

    # srcFile = resultFile
    # resultFile = destFile.replace(".html","_classupdated.html")
    # parser.removeIds(frw.readFile(srcFile),resultFile)