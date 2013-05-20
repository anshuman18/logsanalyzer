#!/usr/bin/python
import re
import sys


class chunk:
    def __init__(self, lines):
        self.data = lines[:]

    def get(self):
        return self.data

    def __hash__(self):
        if(len(self.data)>1):
           return  hash(self.data[1]);
        return 42

    def __eq__(self,other):
        if(len(self.data)>1 and len(other.data)>1):
            return   hash(self.data[1])== hash(other.data[1]);
        return false

def readConfFile(fileName):
    lines=[]
    fo = open(fileName,"r")
    try:
        for line in fo:
            lines.append(line.rstrip('\n\r'))
    finally:
        fo.close()

    return lines

def match(line, ptrns):
    for ptrn in ptrns:
        if (re.search(ptrn,line)):
            return 1
    return 0

def appendChunks(chnks,matchLines):
    if(len(matchLines)==0):
        return

    chnk = chunk(matchLines)
    if (chnk in chnks):
       chnks[chnk]+=1
    else:
       chnks[chnk]=1

def processBuffer(buff, offset, chnks, matchLines):
    for line in buff:
        if(offset!=0):
            if (match(line, endptrns) == 1):
                appendChunks(chnks,matchLines)
                matchLines = []
                offset = 0
                if (match(line,startptrns) == 1):
                    matchLines.append(line)
                    offset=1
            else:
                matchLines.append(line)
        else:
            if (match(line,startptrns) == 1):
                matchLines = []
                matchLines.append(line)
                offset=1

    appendChunks(chnks,matchLines)
    return matchLines, offset


def processFile(inFileName):
    buff=[]
    bsz=500
    c=0
    offset=0
    chnks={}
    matchLines = []
    fo = open(inFileName,"r")
    try:
        for line in fo:
            line = line.strip()
            if(not line):
                continue
            if(c==bsz):
                matchLines, offset = processBuffer(buff, offset, chnks, matchLines)
                buff=[]
                c=0
            else:
                buff.append(line.rstrip('\n\r'))
                c+=1
        if(len(buff)>0):
            processBuffer(buff, offset, chnks, matchLines)
    finally:
        fo.close()

    return chnks

def dumpChnks(chnks, outFldr, lgFile):
    i=0
    if(lgFile.rindex("/")!=-1):
       i=lgFile.rindex("/")
    elif(lgFile.rindex("\\")!=-1):
       i=lgFile.rindex("\\")

    outFile = outFldr + lgFile[i:] + ".xml"
    sorteddict_byValue = [x for x in chnks.items()]
    sorteddict_byValue.sort(key=lambda x: x[1]) # sort by value
    sorteddict_byValue.reverse()
    fw = open (outFile,"w")
    try:
        for cn in sorteddict_byValue:
           fw.write("<chunk>\n")
           fw.write("<content>\n")
           for line in cn[0].get():
               fw.write(line+'\n')
           fw.write("</content>\n")
           fw.write("<count>")
           fw.write(str(cn[1]))
           fw.write("</count>\n")
           fw.write("</chunk>\n")
    finally:
        fw.close()

def process(lgConfFile, outFldr):
    lgFiles = readConfFile(lgConfFile)

    if(len(lgFiles)>0):
        for lgFile in lgFiles:
            chnks = processFile(lgFile)
            if(len(chnks)>0):
                dumpChnks(chnks, outFldr, lgFile)


# main
if len(sys.argv)!=3:
    print("Invalid number of arguments passed")
    print ("usage: ./logreport <inLogFl> <outputfolder>")
    sys.exit(-1)

startptrns = ["SEVERE","WARNING", "ERROR", "FATAL"]
endptrns = ["INFO","SEVERE","WARNING", "ERROR", "FATAL"]
lgConfFile = sys.argv[1]
outFldr = sys.argv[2]
process(lgConfFile, outFldr)
print ("done!")    
