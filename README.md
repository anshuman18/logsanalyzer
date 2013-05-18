logsanalyzer
============


logs analyzer tool takes the following configuration as input file
1. logs.in - specify all the folders and the files that need to be searched for patters (folders separated by new line)

for e.g
entries for logs.in
/tmp/anshuman/cluster01/webapp
/tmp/anshuman/cluster02/webapp

This tool will lookup all files with name as *webapp* in follwing folders /tmp/anshuman/cluster01 and /tmp/anshuman/cluster02

2. patterns.in - pattens that need to be searched (patterns separated by new line)
for e.g
entries in patterns.in
NullpointerException
ArrayIndexOutOfBoundException


Invocation
./simpleloganalyzerdriver <in_log_file> <in_pattern_file> <out_folder> <chunksize>

log file analyzer tool will take the following input 
log configuration
patterns configuration files
output folder location 
chunksize

Report summary will be printed on the console with the following information
log files that have matched the patterns
log files that have NOT matched the patterns
chunks with mi=ore that one pattern matches

The output will be list of files with the same name as the input files for any pattern matched. The file contents will be list of chunks of the size specified.








