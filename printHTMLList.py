# Please compile using python3.4
# http://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python
# http://stackoverflow.com/questions/2922783/how-do-you-walk-through-the-directories-using-python

import re
import os
import mimetypes # for finding type of file
import sys
import copy

htmlStringBegin = "<!DOCTYPE html>\n\
<html>\n\
<head>\n\
	<title>Project - Index of Words</title>\n\
	<link href='http://fonts.googleapis.com/css?family=Lato:400,700,900' rel='stylesheet' type='text/css'>\n\
	<link href='http://fonts.googleapis.com/css?family=Roboto:400,700,900' rel='stylesheet' type='text/css'>\n\
	<link rel=\"stylesheet\" href=\"styles/bootstrap/bootstrap.min.css\">\n\
	<link rel=\"stylesheet\" href=\"styles/bootstrap/bootstrap-theme.min.css\">\n\
	<link rel=\"stylesheet\" href=\"styles/myStyle.css\">\n\
	<script type=\"text/javascript\" src=\"js/search.js\"></script>\n\
</head>\n\
<body>\n\
	<div id=\"head-title\">\n\
		<center>\n\
			<p id=\"title\"><b>Index File </b>\n\
			<!--<input type=\"text\" width=\"500px\"></input>\n\
			<button id=\"search\">Search</button></p>-->\n\
			<input id=\"search-word\" name=\"wordToSearch\" type=\"text\" width=\"500px\" onKeyDown=\"if(event.keyCode == 13){searchWord(this.value)};\"></input>\n\
			<button id=\"search-button\" onclick=\"searchWord(document.getElementsByName('wordToSearch')[0].value)\">Search</button>\n\
			<button id=\"disp-button\" onclick=\"printOrigDictionary()\">Original Index</button>\n\
		</center>\n\
	</div><br>\n\
	<!--<hr>-->\n\
	<br><br><center><div id=\"resultBox\"></div></center>\n\
		<div id=\"content\">\n\
		<!--<center><b>Index</b></center>-->\n\
		<center>\n"

htmlStringEnd = "	</center></div><center>\n\
		<p id=\"file-title\"></p>\n\
		<table id=\"codeTable\">\n\
		</table><br><br><br>\n\
	</center>\n\
		\n\
<script src=\"js/jquery/jquery-1.11.3.min.js\"></script>\n\
<!-- Include all compiled plugins (below), or include individual files as needed -->\n\
<script src=\"js/bootstrap/bootstrap.min.js\"></script>\n\
<div id=\"footer\"> \n\
	&copy;&nbsp;2015&nbsp;Designed by <a href=\"http://www.cse.iitb.ac.in/~praneethas/\">Sona Praneeth</a>&nbsp;<a href=\"http://www.cse.iitb.ac.in/~siddarth/\">Siddharth A</a>\n\
</div>\n\
</body>\n\
</html>"

'''
Create fileIndex.html - HTML file containing indexlist
Input: Dictionary of words with key as word and value as dictionary of files as key and values as line nos
Output: [[listOfTextFiles],[listOfHTMLFiles]]
'''
def printToHTMLCompleteList(wordsList, outfile):
	indexFile = open(outfile, 'w')
	indexFile.write(htmlStringBegin)
	indexFile.write("\t\t<table class=\"table\" id=\"indexWords\">\n")
	indexFile.write("\t\t<thead>\n\t\t\t<tr id=\"head\">\n");
	indexFile.write("<th>Word</th><th>File Name</th><th>Line Nos</th></tr></thead>");
	noEntries=15
	for wordInfo in wordsList:
		word = wordInfo[0]
		infoWordList = wordInfo[1]
		lenInfoWordList = len(infoWordList)
		for fileName in infoWordList:
			unixFileName = "/".join(fileName[0].split('\\'))
			# print(os.path.normpath(os.path.relpath(fileName[0], '.')))
			relativeFilePath = os.path.relpath(unixFileName, '.')
			normRelativeFilePath = os.path.normpath(relativeFilePath)
			# print("Relative path: ", relativeFilePath)
			# print("Relative normalize path: ", normRelativeFilePath)
			baseFileNameArray = relativeFilePath.split('/');
			baseFileName = baseFileNameArray[-1]
			lineNoArray = fileName[1]
			lenLineNoArray = len(lineNoArray)
			k = 1
			l = 1
			for lineNo in lineNoArray:
				if(l==1 and k!=lenLineNoArray):
					indexFile.write("\t\t\t"+"<tr>"+"\n\t\t\t\t"+"<td id=\"word\">")
					indexFile.write(word)
					indexFile.write("</td>\n")
					indexFile.write("\t\t\t\t<td id=\"file-name\"><a href=\"#codeTable\" onclick=\"populatePre('"+ normRelativeFilePath+"')\">")
					indexFile.write(baseFileName)
					indexFile.write("</a></td>\n")
					indexFile.write("\t\t\t\t<td id=\"line-nos\">")
					indexFile.write("<a href=\"#");
					indexFile.write(str(lineNo))
					indexFile.write("\" onclick=\"populatePre('"+ normRelativeFilePath+"')\">");
					indexFile.write(str(lineNo))
					indexFile.write("</a>&nbsp;");
					l += 1
					k += 1
				elif(l==1 and k==lenLineNoArray):
					indexFile.write("\t\t\t"+"<tr>"+"\n\t\t\t\t"+"<td id=\"word\">")
					indexFile.write(word)
					indexFile.write("</td>\n")
					indexFile.write("\t\t\t\t<td id=\"file-name\"><a href=\"#codeTable\" onclick=\"populatePre('"+normRelativeFilePath+"')\">")
					indexFile.write(baseFileName)
					indexFile.write("</a></td>\n")
					indexFile.write("\t\t\t\t<td id=\"line-nos\">")
					indexFile.write("<a href=\"#");
					indexFile.write(str(lineNo))
					indexFile.write("\" onclick=\"populatePre('"+normRelativeFilePath+"')\">");
					indexFile.write(str(lineNo))
					indexFile.write("</a>");
					indexFile.write("</td>\n")
					indexFile.write("\t\t\t</tr>\n")
					l = 1
					k = 1
				elif(l%noEntries!=0 and k!=lenLineNoArray):
					indexFile.write("<a href=\"#");
					indexFile.write(str(lineNo))
					indexFile.write("\" onclick=\"populatePre('"+ normRelativeFilePath+"')\">");
					indexFile.write(str(lineNo))
					indexFile.write("</a>&nbsp;");
					l += 1
					k += 1
				elif(l%noEntries!=0 and k==lenLineNoArray):
					indexFile.write("<a href=\"#");
					indexFile.write(str(lineNo))
					indexFile.write("\" onclick=\"populatePre('"+ normRelativeFilePath+"')\">");
					indexFile.write(str(lineNo))
					indexFile.write("</a>");
					indexFile.write("</td>\n")
					indexFile.write("\t\t\t</tr>\n")
					l += 1
					k = 1
				elif(l%noEntries==0):
					indexFile.write("<a href=\"#");
					indexFile.write(str(lineNo))
					indexFile.write("\" onclick=\"populatePre('"+ normRelativeFilePath+"')\">");
					indexFile.write(str(lineNo))
					indexFile.write("</a>");
					indexFile.write("</td>\n")
					indexFile.write("\t\t\t</tr>\n")
					l = 1
					k += 1
	indexFile.write("</table>")
	indexFile.write(htmlStringEnd)


'''
Get List of all files in a directory and its subdirectories
Input: Root Directory
Output: [[listOfTextFiles],[listOfHTMLFiles]]
'''
def getAllFilesinDir(directory):
	print('Reading from ', end='')
	print(directory)
	h = 0
	t = 0
	f = 0
	textFilesToTraverse=[]
	htmlFilesToTraverse=[]
	filesToTraverse=[]
	# traverse root directory, and list directories as dirs and files as files
	for root, dirs, files in os.walk(directory):
		for file in files:
			mime = mimetypes.guess_type(file)
			typeOfFile = mime[0]
			if(typeOfFile is None):
				pass
			else:
				type = typeOfFile.split('/')
				if(type[0]=='text'):
					if(type[1]=='plain'):
						absPath = os.path.normpath(os.path.abspath(root+'/'+file))
						textFilesToTraverse.append(absPath)
						t=t+1
					if(type[1]=='html'):
						absPath = os.path.normpath(os.path.abspath(root+'/'+file))
						htmlFilesToTraverse.append(absPath)
	filesToTraverse.append(textFilesToTraverse)
	filesToTraverse.append(htmlFilesToTraverse)
	return filesToTraverse
