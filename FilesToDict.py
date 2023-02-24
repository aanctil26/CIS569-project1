import os
import glob
import json

fileDict = {"CIA":{}, "DIA":{}, "FBI":{}, "NSA":{}, "USCBP":{}}
for infile in glob.glob(os.path.join("./dataset", '*')):
    if(infile.endswith(".txt")):
        continue
    review_file = open(infile,'r').read()
    subKey = infile.split("/")[-1]
    mainKey = subKey.split("_")[0]
    fileDict[mainKey][subKey] = review_file

with open('CIS569data.json', 'w') as fp:
    json.dump(fileDict, fp)

