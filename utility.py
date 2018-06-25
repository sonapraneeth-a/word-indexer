import sys, getopt, os, time

# Color Class
class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

# Global Variables
verbose = False
indir = ""
outfile = ""
argCorrect = False
minifyOpt = False
allParameterCorrect = False

def helpString():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(color.BOLD+"USAGE MAN PAGE"+color.END+"\n")
	print(color.BOLD+"NAME\n\t"+color.END+"indexBuilder\n")
	print(color.BOLD+"AUTHORS\n\t"+color.END+"Praneeth A S, Siddharth A\n")
	print(color.BOLD+"SYNOPSIS\n\t"+color.END+"python3.4 main.py [option]\n")
	print(color.BOLD+"DESCRIPTION"+color.END)
	print("\tIndex Utility\n")
	print(color.BOLD+"OPTIONS"+color.END)
	print(color.BOLD+"   Option Syntax"+color.END)
	print(color.BOLD+"\t--verbose"+color.END)
	print(color.BOLD+"\t-v"+color.END)
	print("\tDisplays the detailed information of the code being run.\n")
	print(color.BOLD+"\t--in-dir=\"<inputDirectory>\""+color.END)
	print(color.BOLD+"\t-i \"<inputDirectory>\""+color.END)
	print("\tUse this to give the name of directory(enclosed in double quotes) for which you want to make the index.\n");
	print(color.BOLD+"\t--out-file=\"<indexFileName.html>\""+color.END)
	print(color.BOLD+"\t-o \"<indexFileName.html>\""+color.END)
	print("\tUse this to give the filename(enclosed in double quotes) of the index made in html.");
	print(color.BOLD+"\tDefault: "+color.END+"index.html\n")
	print(color.BOLD+"\t--help"+color.END)
	print(color.BOLD+"\t-h"+color.END)
	print("\tDisplays the help information for the file.\n")

def printUnknownOption():
	print(color.RED+"Unknown command detected."+color.END);
	print("Please use "+color.BOLD+"python3.4 main.py -h"+color.END+" for more help")
	print(color.BOLD+"Correct Usage:"+color.END)
	print("\tFirst Line - Long form, Next Line - Short form")
	print("\tpython3.4 main.py --in-dir=\"<inputDirectory>\"")
	print("\tpython3.4 main.py -i \"<inputDirectory>\"")
	print("\tpython3.4 main.py --in-dir=\"<inputDirectory>\" --out-file=\"<outputFile>\"")
	print("\tpython3.4 main.py -i \"<inputDirectory>\" -o \"<outputFile>\"")
	print("\tpython3.4 main.py --help")
	print("\tpython3.4 main.py -h")
	print("\tpython3.4 main.py --verbose")
	print("\tpython3.4 main.py -v")

def getArguments(argv):
	if( len(argv)==0 ):
		print(color.RED+"Atleast one argument needed. Please use -h for more information"+color.END)
		sys.exit()
	try:
		opts, args = getopt.getopt(argv, 'hvmi:o:', ['help', 'verbose', 'minify', 'in-dir=', 'out-file='])
	except getopt.GetoptError:
		printUnknownOption()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h' or opt == '--help':
			helpString()
			sys.exit()
		elif opt in ("-i", "--in-dir"):
			global indir
			if not arg:
				print(color.RED+"Input directory is not given"+color.END)
				sys.exit()
			else:
				indir = arg
				global argCorrect
				argCorrect = True
		elif opt in ("-o", "--out-file"):
			global outfile
			if not arg:
				print(color.BLUE+color.BOLD+"Output HTML file name not given.");
				print("So please check "+color.GREEN+"index.html"+color.BLUE+"if everything works fine."+color.END);
				outfile = "index.html"
			else:
				outfile = arg
		elif opt in ("-v", "--verbose"):
			global verbose
			verbose = True
		elif opt in ("-m", "--minify"):
			global minifyOpt
			minifyOpt = True
		else:
			printUnknownOption()
			sys.exit(2)
	if argCorrect and outfile=="":
		allParameterCorrect = True
		print(color.BLUE+color.BOLD+"Output HTML file name not given.");
		print("So please check "+color.GREEN+"index.html"+color.BLUE+" if everything works fine."+color.END);
		outfile = "index.html"
	elif not argCorrect:
		sys.exit()
	else:
		if not os.path.isdir(indir):
			print(color.RED+"Directory "+indir+" doesn't exist.");
			print("Please ensure that "+indir+" is present in the current directory."+color.END)
			sys.exit()
		else:
			filename, file_extension = os.path.splitext(outfile)
			if file_extension!=".html":
				print(color.RED+"Extension of out-file "+outfile+" should be html"+color.END)
				sys.exit()
			else:
				allParameterCorrect = True
	return allParameterCorrect


def verbosePrint(statement, verbose):
	if verbose:
		print(statement)

def debugPrint(statement, debug):
	if debug:
		print(statement)

