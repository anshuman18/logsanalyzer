#!/usr/bin/python
import unittest
import scripts

class TestReport(unittest.TestCase):
    def setUp(self):
        self.rp = scripts.Report()
        self.c = scripts.chunk()
        self.c2 = scripts.chunk()

        self.c.append("anshubo is a nice boy")
        self.c.append("mahatma is indian origin went on to become global figure")
        self.c.append("success is not the destination but a journey")
        self.c.append("atal bihari vajpaee was the prime minister of india")
        self.c.append("failure and success is not the destination but a journey")
        self.c.addTag("mahatma")
        self.c.addTag("atal")
        self.c.addTag("mahatma")
        clist = []
        clist.append(self.c)
        

        self.c2.append("garbage collection algorithm in java has been optimized")
        clist2=[]
        clist2.append(self.c2) 
        
        self.rp.addMatchedFile("anshu.log",clist)
        self.rp.addUnMatchedFile("avi.log")
        self.rp.addMatchedFile("sharma.log",clist2)
        self.rp.addUnMatchedFile("kubar.log")


    def tearDown(self):
        self.rp = None
        self.c2 = None 
        self.c1 = None 

    def test_matchedfile__size(self):
        self.assertEquals( len(self.rp.getMatchedFiles()) , 2)  

    def test_unmatchedfile_size(self):
        self.assertEquals( len(self.rp.getUnMatchedFiles()) , 2)

    def test_tag_size(self):
        self.assertEquals( len(self.rp.getMatchedChunks()) , 1)

    def test_one (self):
        self.assertTrue(True)
    
if __name__ == '__main__':
        unittest.main()
