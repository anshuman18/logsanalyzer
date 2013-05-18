#!/usr/bin/python
import scripts

lgConfFile = ""
ptrnConfFile = ""
outFldr = ""
chnksz= 5

inFileName = "/export/home/anshuman.kumar/loganalyzer2/io/in/sample2.in"
ptrns = ["algorithm","performance","NullPointerException"]

p = scripts.SimpleLogAnalyzer(lgConfFile, ptrnConfFile, outFldr, chnksz)
chnks = p.processFile( inFileName, ptrns, chnksz)
for c in chnks:
    print (c.serialize())

print("done!")


