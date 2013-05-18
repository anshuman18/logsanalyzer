#!/usr/bin/python
import os
import re

class FileUtil:
    def readAllLines(self,inFileName):
        lines=[]
        fo = open(inFileName,"r")
        try:
            for line in fo:
                if(len(line.strip())>0):
                    lines.append(line.rstrip('\n\r'))
        finally:
            fo.close()
        return lines

    def readNextBuffer(self,inFileName, bufsize):
        buf = []
        fo = open(inFileName,"r")
        c = bufsize
        try:
            for line in fo:
                buf.append(line.rstrip('\n\r'))
                c-=1
                if (c<=0):
                    buf2 = buf[:]
                    buf = []
                    c=bufsize
                    yield buf2
        except:
            fo.close()
        fo.close()   
        
        if(len(buf)>0):
            yield buf 
    
    def listDir(self,inFolderName, p):
        files=[]
        for file in os.listdir(inFolderName):
            if(re.search(p, file)):
                files.append( inFolderName + "/" +  file)
        return files

    def listDir2(self,inFolderName, patterns):
        files=[]
        for file in os.listdir(inFolderName):
            for p in patterns:
                if(re.search(p, file)):
                    files.append(file)
        return files

    def writeContents(self, inFileName, contents):
        fw = open(inFileName, "a")
        try:
            fw.write(contents)
        finally:
            fw.close()
  

    def writeLines(self,inFileName,lines):
        fw = open(inFileName,"a")
        try:
            fw.write("<chunk>\n")            
            for line in lines:
                fw.write(line + "\n")
            fw.write("</chunk>\n")    
        finally:
            fw.close()
    
