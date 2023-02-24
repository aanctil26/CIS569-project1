# Import required libraries
import os
import glob
import json

# Initialize dictionary
fileDict = {"CIA":{}, "DIA":{}, "FBI":{}, "NSA":{}, "USCBP":{}}

# Iterate through files, if not correct file (.txt extension) then skip, otherwise add to correct location in dictionary
for infile in glob.glob(os.path.join("./dataset", '*')):
    if(infile.endswith(".txt")):
        continue
    review_file = open(infile,'r').read()
    subKey = infile.split("/")[-1]
    mainKey = subKey.split("_")[0]
    fileDict[mainKey][subKey] = review_file

# Export dictionary to json file
with open('CIS569data.json', 'w') as fp:
    json.dump(fileDict, fp)

