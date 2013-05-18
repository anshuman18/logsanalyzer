#!/usr/bin/python
import chunk
 
class Report:
    def __init__(self):
        self.matchedfiles= []
        self.unmatchedfiles = [] 
        self.matchedchunks = {}
    
    def addUnMatchedFile(self,filename):
         self.unmatchedfiles.append(filename)

    def addMatchedFile(self,filename, chunks):
         self.matchedfiles.append(filename)
         for c in chunks:
             if len(c.getTags())>1 :
                 self.appendChunk(c, filename)  
     
    def getMatchedFiles(self):
        return self.matchedfiles

    def getUnMatchedFiles(self):
        return self.unmatchedfiles

    def appendChunk(self,c, filename):
        if (not filename in self.matchedchunks):
             self.matchedchunks[filename]=[]
        self.matchedchunks[filename].append(c)               

    def getMatchedChunks(self):
        return self.matchedchunks

    def printReport(self):
        print ("<report>")
        if( len (self.unmatchedfiles)> 0): 
            print ("unmatched files :")
            for ufile in self.unmatchedfiles:
                print (ufile)      
        
        if(len (self.matchedfiles)> 0):
            print ("\nmatched files :")
            for ufile in self.matchedfiles:
                print (ufile)
        
        if( len(self.matchedchunks)> 0) :
             print("************found match report************")
             for filename in self.matchedchunks.keys():
                  print("+++++matches for " + filename + "+++++++\n") 
                  for c in self.matchedchunks[filename]: 
                      print (c.serialize()+ "\n")    
        print ("</report>")  


