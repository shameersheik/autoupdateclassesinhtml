import filereadwrite as frw

def updateDestFile(srcSoupMap,destSoup,destFilename):
    for tag in destSoup.find_all():
        tagId = tag['id']
        if(srcSoupMap.__contains__(tagId)):
            tagSrcClasses = srcSoupMap[tagId]
            #classes changed
            if tag.has_attr('class'):
                tagDestClasses = tag['class']
            
            #length not the same
            if(len(tagSrcClasses)) == len(tagDestClasses):
                for i in range(0,len(tagSrcClasses)):
                    if(tagSrcClasses[i] != tagDestClasses[i]):
                        printChanges(srcSoupMap,tag,tagId)
                        tag['class'] = " ".join(tagSrcClasses)
                        printChanged(tag)
                        break
            else:
                printChanges(srcSoupMap,tag,tagId)
                tag['class'] = " ".join(tagSrcClasses)
                printChanged(tag)
                
        #class attr removed
        elif tag.has_attr('class'):
            print("Class removed")
            del tag['class']
            printChanged(tag)

    frw.writeFile(destFilename,destSoup.prettify())

def printChanges(srcSoupMap,tag,tagId):
    print("\n\n")
    print("Source")
    print(tagId)
    print(" ".join(srcSoupMap[tagId]))
    print("dest")
    print(tag["id"])
    print(" ".join(tag["class"]))

def printChanged(tag):
    print("\n")
    print("Changed dest")
    print(str(tag).split(">")[0]+">")
