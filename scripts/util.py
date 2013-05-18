#!/usr/bin/python
import re

def getLastPathIndx( inputstr ):
    lindx = 0
    if(inputstr.rfind("/")!=-1):
        lindx = inputstr.rfind("/")
    elif(inputstr.rfind("\\")!=-1):
        lindx = inputstr.rfind("\\")
    return lindx

def match( line, ptrns ):
    for ptrn in ptrns:
        if (re.search(ptrn,line, re.I)):
            return ptrn
    return None





