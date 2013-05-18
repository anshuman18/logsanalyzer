#!/usr/bin/python
from simpleloganalyzer import *

# main
if len(sys.argv)!=5:
    print("Invalid number of arguments passed")
    print ("usage: ./simpleloganalyzer <in_log_file> <in_pattern_file> <out_folder> <chunksize>")
    sys.exit(-1)

lgConfFile = sys.argv[1]
ptrnConfFile = sys.argv[2]
outFldr = sys.argv[3]
chnksz= int(sys.argv[4])

p = SimpleLogAnalyzer(lgConfFile, ptrnConfFile, outFldr, chnksz)
p.process()
p.generateReport()
print ("done!")
