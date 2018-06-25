import fileinput

def minifyFile(infile, outfile):
	if infile==outfile:
		for line in fileinput.input(infile, inplace=True):
			linesNew=line.replace("\t", "")
			linesNew=linesNew.replace("\n", "")
			print(linesNew,end='')
	else:
		inFile = open(infile, "r")
		outFile = open(outfile, "w")
		for lines in inFile:
			linesNew=lines.replace("\t", "")
			linesNew=linesNew.replace("\n", "")
			outFile.write(linesNew)
		inFile.close()
		outFile.close()