# Please compile using python3.4
# http://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python
# http://stackoverflow.com/questions/2922783/how-do-you-walk-through-the-directories-using-python

import re
import os
import mimetypes # for finding type of file
import sys
import copy

def printToText(wordsList):
	indexFile = open('HTML Index Files/fileDict.txt', 'w')
	for wordInfo in wordsList:
		word = wordInfo[0]
		infoWordList = wordInfo[1]
		lenInfoWordList = len(infoWordList)
		noEntries = 15
		for fileName in infoWordList:
			relativeFilePath = os.path.relpath(fileName[0], './HTML Index Files/')
			baseFileNameArray = relativeFilePath.split('/');
			baseFileName = baseFileNameArray[-1]
			lineNoArray = fileName[1]
			lenLineNoArray = len(lineNoArray)
			k = 1
			l = 1
			for lineNo in lineNoArray:
				if(l==1 and k!=lenLineNoArray):
					indexFile.write(word)
					indexFile.write(", ")
					indexFile.write(relativeFilePath)
					indexFile.write(", ")
					indexFile.write(str(lineNo))
					indexFile.write(" ")
					l += 1
					k += 1
				elif(l==1 and k==lenLineNoArray):
					indexFile.write(word)
					indexFile.write(", ")
					indexFile.write(relativeFilePath)
					indexFile.write(", ")
					indexFile.write(str(lineNo))
					indexFile.write("\n")
					l = 1
					k = 1
				elif(l%noEntries!=0 and k!=lenLineNoArray):
					indexFile.write(str(lineNo))
					indexFile.write(" ")
					l += 1
					k += 1
				elif(l%noEntries!=0 and k==lenLineNoArray):
					indexFile.write(str(lineNo))
					indexFile.write("\n")
					l += 1
					k = 1
				elif(l%noEntries==0):
					indexFile.write(str(lineNo))
					indexFile.write("\n")
					l = 1
					k += 1
