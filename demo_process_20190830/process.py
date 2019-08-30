#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

outFileName = 'output.txt'
finalFileName = 'finalFile.txt'
#uniqueFileName = 'uniqueFile_30.txt'
sameFileName = 'sameFile.txt'

numPat = re.compile(r'\d+\n')
#numPat = re.compile(r'\r\n')
newLinePat = re.compile(r'\n')
#str0Pat = re.compile('\d{2}:\d{2}:\d{2}')
#str1Pat = re.compile('\¿\d*\¿')
#str1Pat = re.compile(r'\(\d*\)')
str2Pat = re.compile(r'\*\n')

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
            #tmp0Str = re.sub(str0Pat, '()', line)
            #tmp1Str = re.sub(str1Pat, '()', tmp0Str)
            #tmp2Str = re.sub(str2Pat, '', tmp1Str)
            tmp2Str = re.sub(str2Pat, '', line)
            result = re.sub(newLinePat, '', tmp2Str)
            outfile.write(result)

def main():
    print("====================")
    print("The data should save in txt file and UTF-8 encode")
    print("Put the txt file in ./data/ directory")
    print("output temp file name", outFileName)
    print("final file name", finalFileName)
    print("Begin process data")

    compare_length = 40
    if len(sys.argv) > 1:
        compare_length = int(sys.argv[1])

    uniqueFileName = 'uniqueFile_' + str(compare_length) + '.txt'

    outfiles = open(outFileName, mode='w', encoding='utf-8')
    finalfiles = open(finalFileName, mode='w', encoding='utf-8')
    uniquefiles = open(uniqueFileName, mode='w', encoding='utf-8')
    samefiles = open(sameFileName, mode='w', encoding='utf-8')
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

    outfiles.write('\n') 
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

    #judge the length of item,if the length is the same, 
    #the item may be the same as to different sort of choices
    lengthPre = 0
    itemPre = ''
    lengthCur = 0
    numSeq = 1
    for item in finalItems:
        lengthCur = len(item)
        print("the length of current item:", lengthCur)
        print("the length of previous item:", lengthPre)
        if (((lengthPre != lengthCur)
            and (itemPre[0:min(lengthPre,lengthCur) - 3] != item[0:min(lengthPre,lengthCur) - 3]))
                or 
                (itemPre[:min(lengthPre,lengthCur, compare_length)] != item[:min(lengthPre,lengthCur, compare_length)])):
            uniquefiles.write(item)
        else:
            print("They are the same item as to different order")
            samefiles.write(str(numSeq) + itemPre)
            samefiles.write(str(numSeq) + item)
            numSeq = numSeq + 1
        lengthPre = lengthCur
        itemPre = item


    print("====================")
    print("End process data")

if __name__ == "__main__":
    main()
