from bs4 import BeautifulSoup
import uuid

PREFIX_ID = "genId_"

def setIds(text,destfile):
    soup = BeautifulSoup(text,'html.parser')
    for tag in soup.find_all():
        if(not tag.has_attr('id')):
            tag['id'] = PREFIX_ID+ str(uuid.uuid4())
    with open(destfile,"w") as writeFile:
        writeFile.write(soup.prettify())

def removeIds(text,destfile):
    soup = BeautifulSoup(text,'html.parser')
    for tag in soup.find_all():
        if(tag.has_attr('id') and tag['id'].startswith(PREFIX_ID)):
            del tag['id']
    with open(destfile,"w") as writeFile:
        writeFile.write(soup.prettify())

def getSoup(text):
    return BeautifulSoup(text, 'html.parser')

def getIdClassMap(text):
    soup = getSoup(text)
    idValues = {}
    for tag in soup.find_all():
        if(tag.has_attr('class')):
            idValues[tag['id']] = tag['class']
    return idValues

