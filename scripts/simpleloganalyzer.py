#!/usr/bin/python
import sys
from report import Report
from fileutil import FileUtil
from util import *
from chunk import chunk
from ringbuffer import RingBuffer

class SimpleLogAnalyzer:
    def __init__(self, lgConfFile, ptrnConfFile, outFldr, chnksz):
        self.lgConfFile = lgConfFile
        self.ptrnConfFile = ptrnConfFile
        self.outFldr = outFldr
        self.chnksz = chnksz
        self.rep = Report()
        self.fu = FileUtil()  

    def getLogFiles(self):
        files =[]
        folders =  self.fu.readAllLines(self.lgConfFile);
        for fldrName in folders:
            lindx = getLastPathIndx( fldrName )
            fldr = fldrName[0:lindx]
            ptrn = fldrName[lindx+1:]
            files+=self.fu.listDir( fldr, ptrn ) 
        return files

    def copy(self,rb,chunks,found):
        chnk = chunk()
        chnk.addTag(found)
        chunks.append(chnk)
        for rbel in rb.get():
           if(rbel!=None):
               chnk.append(rbel) 

    def processBuffer(self,buff, ptrns, offset, chnksz, chnks,rb):
        cLastIndx = len(chnks) - 1
        for line in buff:
            if(offset>0):
                chnks[cLastIndx].append(line)
                found = match(line,ptrns)
                offset-=1 
                if(found != None):
                    chnks[cLastIndx].addTag(found)
            else:
                rb.append(line)
                found = match(line,ptrns)
                if(found != None):
                    self.copy(rb,chnks,found)
                    cLastIndx+=1
                    offset=chnksz
        return offset

    def processFile(self,inFileName, ptrns, chnksz):
        bsz = chnksz * 20
        offset=0
        chnks=[]
        rb = RingBuffer(chnksz) 
        buffitr = self.fu.readNextBuffer(inFileName, bsz)
        for buff in buffitr:
            offset = self.processBuffer(buff,ptrns,offset,chnksz,chnks,rb) 
        return chnks

    def dumpChnks(self, chnks, outFldr, lgFile):
        i=getLastPathIndx(lgFile)
        outFile = outFldr + lgFile[i:] + ".xml"
        for cn in chnks:
            self.fu.writeContents(outFile, cn.serialize())

    def process(self):
        lgFiles = self.getLogFiles()
        ptrns = self.fu.readAllLines(self.ptrnConfFile)
        if(len(lgFiles)>0 and len(ptrns)>0):
            for lgFile in lgFiles:
                chnks = self.processFile(lgFile, ptrns, self.chnksz)
                if(len(chnks)>0):
                    self.rep.addMatchedFile(lgFile,chnks)
                    self.dumpChnks(chnks, self.outFldr, lgFile)
                else:
                    self.rep.addUnMatchedFile(lgFile)  


    def generateReport(self):
        self.rep.printReport()

