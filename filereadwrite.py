def readFile(filename):
    with open(filename,"r") as readfile:
        return readfile.read()

def writeFile(filename,content):
    with open(filename,"w") as writefile:
        writefile.write(content)