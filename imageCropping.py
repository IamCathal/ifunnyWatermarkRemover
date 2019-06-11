from PIL import Image
import shutil
import re
import os


def main():
    getImageCounter()
    cleanNames()
    moveFiles()


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

    for meme in memes:
        shutil.move(source+meme, dest)

    print("Files moved!")


def cleanNames():
    lastFile = ""
    memeRegEx = '^(meme)+'
    memeCount = getImageCounter() + 1

    for fileName in os.listdir("rawFiles"):
        if not re.match(memeRegEx, fileName):
            newString = 'meme'+str(memeCount)+'.jpg'
            newString = 'rawFiles/'+newString
                
            src = 'rawFiles/'+fileName
            
            os.rename(src, newString)
            cropImage(newString)
            memeCount += 1

    print("Files cropped!")


if __name__ == '__main__':
    main()