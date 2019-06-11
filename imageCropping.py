from PIL import Image
import shutil
import re
import os


def main():
    makeDirs()
    getImageCounter()
    cleanNames()
    moveFiles()


def makeDirs():
    rawDir = 'rawFiles'
    croppedDir = 'croppedFiles'
    
    if not os.path.exists(rawDir):
        os.mkdir(rawDir)

    if not os.path.exists(croppedDir):
        os.mkeir(croppedDir)


def getImageCounter():
    i = 0

    for file in os.listdir("croppedFiles"):
        i += 1

    return i


def cropImage(imageName):
    imObj = Image.open(imageName)
    croppedHeight = imObj.size[1] - 21
    croppedSize = (0, 0, imObj.size[0], croppedHeight)

    croppedRegion = imObj.crop(croppedSize)
    croppedRegion.save('{}'.format(imageName), "JPEG")


def moveFiles():
    source = 'rawFiles/'
    dest = 'croppedFiles/'
    memes = os.listdir(source)
    fileMoved = 0

    for meme in memes:
        shutil.move(source+meme, dest)
        fileMoved += 1

    if fileMoved:
        print("{} files moved!".format(fileMoved))


def cleanNames():
    lastFile = ""
    memeRegEx = '^(meme)+'
    memeCount = getImageCounter() + 1
    memeCropped = 0

    for fileName in os.listdir("rawFiles"):
        if not re.match(memeRegEx, fileName):
            newString = 'meme'+str(memeCount)+'.jpg'
            newString = 'rawFiles/'+newString
                
            src = 'rawFiles/'+fileName
            
            os.rename(src, newString)
            cropImage(newString)
            memeCropped += 1
            memeCount += 1

    if memeCropped:
        print("{} files cropped!".format(memeCropped))


if __name__ == '__main__':
    main()