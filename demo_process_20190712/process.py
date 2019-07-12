#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

outFileName = 'output.txt'
finalFileName = 'finalFile.txt'

numPat = re.compile(r'\d+\n')
#numPat = re.compile(r'\r\n')
newLinePat = re.compile(r'\n')
str0Pat = re.compile('\d{2}:\d{2}:\d{2}')
#str1Pat = re.compile('\¿\d*\¿')
str1Pat = re.compile('\(\d*\)')
str2Pat = re.compile('\(\d*\)')

def getData(infile, outfile):
    print("in getData")
    for line in infile:
        #print "the file context every line: ", line
        context = numPat.findall(line)
        # First replace the item number to \n
        if len(context) and len(line) < 10:
            result = re.sub(numPat, '', line)
            outfile.write('\n')
        else:
           # Replace the (015)(015) every line to unique
            tmp0Str = re.sub(str0Pat, '()', line)
            tmp1Str = re.sub(str1Pat, '()', tmp0Str)
            tmp2Str = re.sub(str2Pat, '()', tmp1Str)
            result = re.sub(newLinePat, '', tmp2Str)
            outfile.write(result)

def main():
    print("====================")
    print("The data should save in txt file and UTF-8 encode")
    print("Put the txt file in ./data/ directory")
    print("output temp file name", outFileName)
    print("final file name", finalFileName)
    print("Begin process data")
    outfiles = open(outFileName, mode='w', encoding='utf-8')
    finalfiles = open(finalFileName, mode='w', encoding='utf-8')
    files = []
    files = os.listdir("./data/") 
    files.sort()
    totalItems = []
    finalItems = []

    for myFile in files:
        print("To process files:", myFile)
        pos = myFile.rfind("txt", len(myFile) - 3, len(myFile))
        if pos > -1:
            infiles = open("./data/" + myFile, mode='r', encoding='utf-8')
            getData(infiles, outfiles)
            print("Finish process files:", myFile)
        else:
            print("GOT YOU ! NOT txt file", myFile)

    outfiles.close() 
    outfiles = open(outFileName, mode='r', encoding='utf-8')

    for item in outfiles:
        totalItems.append(item)

    #for python 2.7
    #finalItems = {}.fromkeys(totalItems).keys()
    #finalItems.sort()

    #for python 3.x
    finalItems = sorted({}.fromkeys(totalItems))
    for item in finalItems:
        finalfiles.write(item)

    print("====================")
    print("End process data")

if __name__ == "__main__":
    main()
