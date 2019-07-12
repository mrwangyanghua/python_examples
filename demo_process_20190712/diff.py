#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

def main():
    print("====================")
    #python 2.7 support raw_input, python 3.x only support input
    #outFileName = raw_input("input output diff filename, like diffV1.txt: ");
    outFileName = input("input output diff filename, like diffV1.txt: ");
    print("Get data from the filename V1 to V2, the output file is: ", outFileName)
    fileNameV1 = input("input filename for V1(older) in current directory, like finalFileV1.txt: ");
    print("filename for V1: ", fileNameV1)
    fileNameV2 = input("input filename for V2(newer) in current directory, like finnalFileV2.txt: ");
    print("filename for V2: ", fileNameV2)

    infileV1 = open(fileNameV1, mode='r', encoding='utf-8')
    infileV2 = open(fileNameV2, mode='r', encoding='utf-8')
    outFile = open(outFileName, mode='w', encoding='utf-8')

    itemsV1 = []
    itemsOut = []

    for itemV1 in infileV1:
        itemsV1.append(itemV1)
        #print(itemV1)

    for itemV2 in infileV2:
        if itemV2 not in itemsV1: 
            outFile.write(itemV2)
            #outFile.write("\n")
        #print(itemV2)
		
    infileV1.close()
    infileV2.close()
    outFile.close()
    print("====================")
    print("Finish getting the diff data\n")

if __name__ == "__main__":
    main()
