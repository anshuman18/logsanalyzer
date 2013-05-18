logsanalyzer
============

logs analyzer tool takes the following configuration as input file
#logs.in - specify all the folders and the files that need to be searched for patters (folders separated by new line)

for e.g
entries for logs.in
/tmp/anshuman/cluster01/webapp
/tmp/anshuman/cluster02/webapp

This tool will lookup all files with name as *webapp* in follwing folders /tmp/anshuman/cluster01 and /tmp/anshuman/cluster02

#patterns.in - pattens that need to be searched (patterns separated by new line)
for e.g
entries in patterns.in
NullpointerException
ArrayIndexOutOfBoundException



