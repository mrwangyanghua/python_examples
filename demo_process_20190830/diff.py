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
    matchFile = open('matchFile.txt', mode='w', encoding='utf-8')

    itemsV1 = []
    itemsV2 = []
    itemsOut = []
    itemsMatch = []

    for itemV1 in infileV1:
        itemsV1.append(itemV1)
        #print(itemV1)

    for itemV2 in infileV2:
        itemsV2.append(itemV2)


#    for itemV2 in infileV2:
#        if itemV2 not in itemsV1: 
#            outFile.write(itemV2)
            #outFile.write("\n")
        #print(itemV2)
		
    lengthV1 = 0
    lengthV2 = 0
    for itemV2 in itemsV2:
        lengthV2 = len(itemV2)

        #print("need match itemV2: ", itemV2)
        for itemV1 in itemsV1:
            lengthV1 = len(itemV1)
            #print("need match itemV1: ", itemV1)
            if ((abs(lengthV1 - lengthV2) <= 2)
                    and (itemV1[:min(lengthV1,lengthV2,40)] == itemV2[:min(lengthV1,lengthV2,40)])
                    ):
                #print("match item: ", itemV2)
                itemsMatch.append(itemV2)
                matchFile.write(itemV2)


            #if (((abs(lengthV1 - lengthV2) >= 2)
            #    and (itemV1[0:min(lengthV1,lengthV2) - 3] != itemV2[0:min(lengthV1,lengthV2) - 3]))
            #    or 
            #    (itemV1[:min(lengthV1,lengthV2,30)] != itemV2[:min(lengthV1,lengthV2,30)])):
            #    outFile.write(itemV2)
            #else:
            #    print("====================")

            
    #print("==================== ==================")
    #for itemV1 in itemsMatch:
    #    print("item of itemMatch:", itemV1)
                
    #print("==================== ==================")
    for item in itemsV2:
        if item not in itemsMatch: 
            outFile.write(item)

    infileV1.close()
    infileV2.close()
    outFile.close()
    print("====================")
    print("Finish getting the diff data\n")

if __name__ == "__main__":
    main()
