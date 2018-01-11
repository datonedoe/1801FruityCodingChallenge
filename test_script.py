import unittest
import script
import setupFolder #to set up folder structure for test cases
import os
import string
import shutil #to do force remove
import random
from random import randint

class TestReadfile(unittest.TestCase):
    def setUp(self):
        print("SETUP")
        self.rootFolder=os.getcwd()
        self.testFolder="testFolder"
        self.testPath=os.path.join(self.rootFolder,self.testFolder)
        if (os.path.isdir(self.testPath)):
            shutil.rmtree(self.testPath)
        os.mkdir(self.testPath)

    def tearDown(self):
        print("TEARDOWN")
        os.chdir(self.rootFolder);
        shutil.rmtree(self.testPath)

    def test_invalidDir(self):
        print("TEST_INVALIDDIR")

        with self.assertRaises(Exception):
            script.findTreasure("./jskghkjb")
            self.assertTrue(true)

        with self.assertRaises(Exception):
            script.findTreasure("=")
            self.assertTrue(true)

        with self.assertRaises(Exception):
            script.findTreasure("./,/k")
            self.assertTrue(true)

    def test_validDirWithNoRegex(self):
        print("TEST_VALIDDIR_WITH_NO_REGEX")
        os.chdir(self.rootFolder);
        referenceFolder = setupFolder.generateFolderContent(self.testFolder)

        os.chdir(self.rootFolder);
        self.assertEqual(referenceFolder, script.findTreasure(self.testFolder))

    def test_validDirWithRegex(self, regex=r"[A-Z]\d[A-Z] \d[A-Z]\d"):
        print("TEST_VALIDDIR_WITH_REGEX")
        os.chdir(self.rootFolder);
        referenceFolder = setupFolder.generateFolderContent(self.testFolder, regex)

        os.chdir(self.rootFolder);
        self.assertEqual(referenceFolder, script.findTreasure(self.testFolder, regex))


if __name__ == "__main__":
    unittest.main()
