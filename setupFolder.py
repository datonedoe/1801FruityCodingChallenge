# import script
import os, re
import string
import random
import rstr
from random import randint
import argparse
import datetime # for random folder name

parser = argparse.ArgumentParser(description="Setup Folder Structure For Testing (c)DatOneDoe 2018 www.datonedoe.com")
parser.add_argument("-r", "--root_dir", metavar="", help="Root directory to start generating files and folders'.'")
parser.add_argument("-k", "--keyword", metavar="", help="Regular expression, DEFAULT: \"^[a-zA-Z]+_TESTResult.*\"")
args=parser.parse_args()

MIN_ITERATION = 200
MAX_ITERATION = 1000
MIN_NUM_FILE_GENERATED = 1
MAX_NUM_FILE_GENERATED = 10
MIN_NUM_FOLDER_GENERATED = 1
MAX_NUM_FOLDER_GENERATED = 3
DEFAULT_REGEX="^[a-zA-Z]+_TESTResult.*"
validFileContents = []

invalidFileContents = [
    'abc',
    'def',
    'hij'
]

def getNewFolderNameList():
    num=randint(MIN_NUM_FOLDER_GENERATED,MAX_NUM_FOLDER_GENERATED)
    folderList=set()
    for index in range(0, num):
        folderList.add(random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase))
    return folderList;


def getNewFileNameList():
    num=randint(MIN_NUM_FILE_GENERATED,MAX_NUM_FILE_GENERATED)
    filenameList=set()
    for index in range(0, num):
        fileExtention=random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
        filenameList.add(random.choice(string.ascii_lowercase)+"." +fileExtention)
    return filenameList;


def generateFolderContent(path=".", keyword=DEFAULT_REGEX):
    root=os.path.abspath(path);
    global validFileContents;

    validFileContents=[]
    for i in range(4):
        validFileContents.append(rstr.xeger(keyword))

    # print("validFileContents", validFileContents)
    currentPath=root;

    actionOptions = ["MKDIR", "CREATE_FILE", "MOVE_DOWN", "MOVE_UP"]
    numOfIterations = randint(MIN_ITERATION, MAX_ITERATION);
    sumValidFile=0;
    sumInvalidFile=0;
    result={}
    for i in range(0, numOfIterations):
        # print("ITERATION #{}/{}: Start>>>>".format(i+1, numOfIterations))
        # print("CURRENT PATH:", currentPath);
        iterationFinished=False;

        while (iterationFinished==False):
            actionIndex = randint(0,len(actionOptions)-1);
            # actionIndex = randint(0,1);
            # print("CRW:", os.getcwd())
            # print("\nAction \"{}\"".format(actionOptions[actionIndex]));
            if (actionIndex==0): #MKDIR

                if (isThereFolderHere(currentPath)==True):
                    pass
                else:
                    newFolderNameList=getNewFolderNameList()
                    # print("newFolderNameList",newFolderNameList)
                    generateFolderBatch(currentPath, newFolderNameList)
                    iterationFinished=True

            if (actionIndex==1): #CREATE_FILE

                if (isThereFileHere(currentPath)==True):
                    pass
                else:
                    newFileNameList=getNewFileNameList()
                    # print("newFileNameList",newFileNameList)
                    tempDict=generateFileBatch(currentPath, newFileNameList,root)
                    for key in tempDict:
                        if tempDict[key]>0:
                            tempKey=key.replace("\\", '/')
                            result.update({tempKey: tempDict[key]})
                    iterationFinished=True

            if (actionIndex==2): #MOVE_DOWN
                if (isThereFolderHere(currentPath)==False):
                    pass
                else:
                    listOfDirectories = getFolderListInDir(currentPath);
                    newFolder=listOfDirectories[randint(0, len(listOfDirectories))-1]
                    # print("New folder", newFolder);
                    currentPath=os.path.abspath(os.path.join(currentPath, newFolder))
                    os.chdir(currentPath)
                    iterationFinished=True


            if (actionIndex==3): #MOVE_UP
                if (currentPath==root):
                    pass
                else:
                    currentPath=os.path.abspath(os.path.join(currentPath, '../'))
                    os.chdir(currentPath)
                    iterationFinished=True


        # print("")
        # print("INTERATION #{}/{}: <<<Finished".format(i+1, numOfIterations))
        # print("----------------------\n")


    os.chdir(root)
    # print("WORKING DIR:", os.getcwd());
    # print("RESULT", result);
#
    # formatResult(result);
    return result;

def shouldValidFileBeCreated():
    return True if randint(0,1)==0 else False

def getRelativePath(currentPath, root):
    commonPrefix = os.path.commonprefix([os.path.join(root, ""), os.path.join(currentPath,"")])
    return os.path.relpath(currentPath, commonPrefix)


def createFile(filename, contentBank):
    f= open(filename,"w+")
    f.write(contentBank[randint(0,len(contentBank)-1)])
    f.close()

def isThereFolderHere(currentPath):
    return True if len(next(os.walk(os.path.abspath(currentPath)))[1])>0 else False

def isThereFileHere(currentPath):
    return True if len(next(os.walk(os.path.abspath(currentPath)))[2])>0 else False

def getFolderListInDir(currentPath):
    return next(os.walk(os.path.abspath(currentPath)))[1];

def getFileListInDir(currentPath):
    return next(os.walk(os.path.abspath(currentPath)))[2];

def generateFolderBatch(currentPath, listOfFolderName):
    for each in listOfFolderName:
        try:
            os.mkdir(os.path.join(currentPath, each))
        except:
            pass

def generateFileBatch(currentPath, listOfFileName, root):
    numFileValid=0
    numFileInvalid=0
    for eachFilename in listOfFileName:
        if shouldValidFileBeCreated() == True:
            createFile(os.path.join(currentPath,eachFilename), validFileContents)
            numFileValid+=1
        else:
            createFile(os.path.join(currentPath,eachFilename), invalidFileContents)
            numFileInvalid+=1
    return {getRelativePath(currentPath, root):numFileValid}

def formatResult(answer):
    for eachKey in sorted(answer):
        print(eachKey, ":", answer[eachKey])

if __name__ == "__main__":
    # listFolderContent(".")
    if args.keyword==None:
        keyword=DEFAULT_REGEX
    else:
        keyword=args.keyword

    if args.root_dir==None:
        root_dir='.'
    else:
        root_dir=args.root_dir

    result=generateFolderContent(root_dir, keyword)
    print(result)
