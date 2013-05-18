#!/usr/bin/python
import unittest
import scripts

class TestFileUtil(unittest.TestCase):
    def setUp(self):
        self.fu = scripts.FileUtil()
        self.p="webapp"
        self.inFolderName = "/export/home/anshuman.kumar/loganalyzer2/io/in"
        self.inFileName =  "/export/home/anshuman.kumar/loganalyzer2/io/in/fortylines.in"

    def a_test_listDir(self):
        files = self.fu.listDir( self.inFolderName, self.p) 
        self.assertEquals( len(files) , 1)
        print (str(files))

    def a_test_readAllLines(self):
        for buf in self.fu.readAllLines(self.inFileName):
            print (str(buf))

    def test_readNextBuffer(self):
        bufitr = self.fu.readNextBuffer(self.inFileName, 5)
        for buf in bufitr:
            print (len(buf))
            for ln in buf:
                print(ln)   

        #for buf in self.fu.readNextBuffer(self.inFileName, 5):
        #    print (str(buf)) 

if __name__ == '__main__':
        unittest.main()

