import sys, getopt, os, time
import populateDict
import printHTMLList
import utility

# Optional
import printToText
import minify

utility.getArguments(sys.argv[1:])

indirName = "Input Directory "+utility.indir;
outputFile = "Output File "+utility.outfile;
utility.verbosePrint(indirName, utility.verbose)
utility.verbosePrint(outputFile, utility.verbose)

# Calculate getAllFilesinDir time
start_time = time.time()
reqFiles = printHTMLList.getAllFilesinDir(utility.indir);
reqFilesTime = time.time() - start_time
stmt = "Function getAllFilesinDir "+str(reqFilesTime)+"sec"
utility.verbosePrint(stmt, utility.verbose)

# Calculate populateDict time
start_time = time.time()
words = populateDict.populateDict(reqFiles);
populateDictTime = time.time() - start_time
stmt = "Function populateDict "+str(populateDictTime)+"sec"
utility.verbosePrint(stmt, utility.verbose)

# Calculate printToHTMLCompleteList time
start_time = time.time()
printHTMLList.printToHTMLCompleteList(words, utility.outfile);
printToHTMLCompleteListTime = time.time() - start_time
stmt = "Function printToHTMLCompleteList "+str(printToHTMLCompleteListTime)+"sec"
utility.verbosePrint(stmt, utility.verbose)

if utility.minifyOpt:
	minify.minifyFile(utility.outfile, utility.outfile)

# ## Optional
# # Calculate printToText time
# # start_time = time.time()
# # printToText.printToText(words);
# # printToTextTime = time.time() - start_time
# # print( 'Function printToText ' , printToTextTime, 'sec')
# # minify.minifyFile("js/search.js", "js/search-min.js")
# # minify.minifyFile("index.html", "index-min.html")
