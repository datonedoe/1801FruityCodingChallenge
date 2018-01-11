## APPLE CODING EXCERCISE

Answer to Apple coding exercise
(c) DatOneDoe 2018 www.datonedoe.com

## GETTING STARTED
The assignment is to write a stand-alone script that should recursively walk the “root_dir” and detect all the files under that dir contains “keywords” and count the number of files for that sub dir. All results should be saved in a key:value array with key being subdir string, and value being counts of file contains the key line. (Due to the answer being uploaded to public Github repo, full version of the problem is not shown here)

## PREREQUISITES
There are couple modules used in this answer that may require being installed on user's computer before executing the files
```
List of modules used: re, os, sys, argparse, operator, mathplotlib, unittest, shutil, rstr, random, string
```

## RECOMMENDED PROCEDURES FOR RUNNING AND TESTING
```
1. Create an empty folder (namely 'playground' in directory containing script.py, setupFolder.py, and test_script.py)
      mkdir playground
2. Run this command line to randomly generate folders and files in 'playground' folder
      python setupFolder.py -r ./playground
3. Run this command line to show a list of directories that contains special regex "[A-9]TestResult"
      python script.py -r ./playground
4. Run this command line perform unit testing (this command can be run by itself without #1, #2, #3 above)
      python test_script.py
5. Remove playground
      rm playground
      [y/n] to remove folder: y
```

#### Demo
[![Watch the video](https://github.com/datonedoe/1801FruityCodingChallenge/blob/master/asset/video.png)]((http://youtu.be/zWi7Mx5ufzw)

## CONTENTS

### script.py
  This is the answer to the asked problem. In the command line, The

  ```
  TO RUN script.py
    python script.py <-r root_dir> <-k keyword>
    Note:
    - root_dir (optional): the directory that the program will be performed on, the default value is the current working directory
    - keyword (optional): is the regular expression to be found, default value is the value given in the problem requirement

    Example:
    python script.py -r ./ -k [A-9]TestResult
    OR
    python script.py -r ./playground -k [A-9]TestResult (assuming ./playground exists and that's the folder to be tested)
  ```
  Example of graph show the distribution of folder path vs numbers of file containing special regex
  ![alt text](https://raw.githubusercontent.com/datonedoe/1801FruityCodingChallenge/master/asset/demo.png)

### setupFolder.py
  Build a folder tree randomly with files that may or may not contain the files with given regular expression. This is used as a reference to compare with the results generated by script.py file

  ```
  TO RUN setupFolder.py
    python setupFolder.py <-r root_dir> <-k keyword>
    Note:
    - root_dir (optional): the directory that the program will be performed on, the default value is the current working directory
    - keyword (optional): is the regular expression to be found, default value is the value given in the problem requirement

    Example:
    python setupFolder -r ./ -k [A-9]TestResult
    OR
    python setupFolder -r ./playground -k [A-9]TestResult (assuming ./playground exists)
  ```

### test_script.py
  Unit testing file for script.py. It utilizes setupFolder to randomly generate folder trees and compare the resulted given by script.py and let the computer perform unit testing.
  ```
  TO RUN test_script.py
    python test_script
  ```
  3 test cases are:
  - Test if directory entered does not exist
  - Test if the regular expression used are the one given by the problem
  - Test if the regular expression is passed by the testFolder

### AUTHORS
#### Darwin Do @datonedoe www.datonedoe.com
