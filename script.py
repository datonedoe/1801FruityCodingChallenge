import re, os, sys
import argparse
import operator
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser(description="Apple Coding Excercise (c)DatOneDoe 2018 www.datonedoe.com")
parser.add_argument("-r", "--root_dir", metavar="", help="Root directory to start traversing, DEFAULT: current directory '.'")
parser.add_argument("-k", "--keyword", metavar="", help="Regular expression to detect a file contains that string, DEFAULT: \"^[a-zA-Z]+_TESTResult.*\"")
args=parser.parse_args()
DEFAULT_REGEX = "[a-zA-Z]+_TESTResult.*";

def findTreasure(rootDir=".", word=DEFAULT_REGEX):
    output={}

    pattern=re.compile(word)
    root=os.path.abspath(rootDir);

    try:
        if(not os.path.isdir(root)):
            raise Exception("Not a valid directory")
    except Exception as e:
        print(e)

    # traverse root directory, and list directories as dirs and files as files
    for dirpath, dirnames, filenames in os.walk(root):
        print("root", root)
        print("Current Path:", dirpath)
        print("Directories:", dirnames)
        print("Files", filenames)
        filecount=0;
        for filename in filenames:
            filename= os.path.join(dirpath, filename)
            # print("FILENAME", filename)
            f=open(filename, encoding="utf-8")
            fileContent=f.read()
            # if pattern.match(fileContent):
            #     print("MATCHHH")
            #     filecount+=1
            if re.search(pattern, fileContent):
                filecount+=1
            f.close()

        if filecount>0:
            temp_path= getRelativePath(dirpath, root)
            temp_path=temp_path.replace("\\", '/')
            output[temp_path] = filecount
        # print("")

    return output

def getRelativePath(currentPath, root):
    commonPrefix = os.path.commonprefix([os.path.join(root, ""), os.path.join(currentPath,"")])
    return os.path.relpath(currentPath, commonPrefix)


def main():
    # print("Current working directory:", os.getcwd())
    link = os.getcwd()

if __name__=="__main__":
    # findTreasure('./playground', "[a-zA-Z]+_TESTResult.*")

    if args.keyword==None:
        keyword=DEFAULT_REGEX
    else:
        keyword=args.keyword

    if args.root_dir==None:
        root_dir='.'
    else:
        root_dir=args.root_dir

    answer=findTreasure(root_dir,keyword)

    for eachKey in sorted(answer):
        print(eachKey, ":", answer[eachKey])

    if answer != None:
        print(answer)

        data=sorted(answer.items());
        sorted_answer = sorted(answer.items(), key=operator.itemgetter(0))
        # print("sorted_answer", sorted_answer)
        x= answer.keys()
        y= answer.values()
        # print(data.items())
        fig = plt.figure()
        ax= fig.gca()
        ax.set_yticks(range(min(y)-1, max(y)+1, 1))
        plt.title('Directories vs Frequency of files containing pre-defined regex\n(c) Datonedoe 2018 www.datonedoe.com', color="C0")
        plt.xlabel('Directories (subdir name string)')
        plt.ylabel("Frequency (count values)")
        for eachPair in sorted_answer:
            plt.scatter(eachPair[0],eachPair[1])
        plt.grid()
        plt.show()
