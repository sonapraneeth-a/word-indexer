# Title

Making Index file (as in the back of book) for a directory.

## Authors

Sona Praneeth Akula, Siddharth A

## Installation

```bash
$ # Requires Python3.4 
$ sudo apt-get install python3-numpy
$ sudo apt-get install python3-scipy python3-matplotlib # for python plots
```

## Running

- For firefox(local running) Place the directory you want to index in HTML Index Files
- For other browsers like Chrome, Use a server and then you have freedom to put the directory anywhere else(but preferably outside HTML Index Files or in HTML Index Files)
- Run the code by typring following command in terminal

```bash
$ python3.4 main.py -h # for help on various options for running project
$ python3.4 main.py -i "indir" # Sample run
```

- Afterwards open finalIndex.html in Firefox. **No Chrome please as it will show security error**
- If you want open to this file on Chrome, please use a web server like apache and copy the entire "HTML Index Files" directory along with the testDirectoy and paste it as it is without changing the location on the server
- This will show the index of entries for all text/html files in the directory/subdirectory
- Type a word in the searchbox to get list of files along with their line nos in their respective files in a table format
- Click on either file/line no to get to the word in the required line in file.(Just scroll three lines upwards to see the exact line)

## Versions used: 

- python3.4.3
- matplotlib 1.3.1: for plotting performance graphs in python, else not required
- numpy 1.8.2
- scipy 0.13.3
- Firefox 42.0 (for client side running)

**NOTE:** Chrome can be used if html and related files are on server


## Files and their description:

```bash
ignoreWords
    Contains list of stop words you might want to ignore while making index
tagList
    Contains list of html tags you might want to ignore while making index for html pages
printHTMLList.py
    Creates fileIndex.html in "HTML Index Files"
createGraph.py
    Creates performance plot for populateDict function - backbone of code
HTML Index Files/finalIndex.html - Generated from main.py
    This file is the file used for searching word
main.py
    Main file for generating dictionary and index file
utility.py
    Utility for verifying command line arguments passed
HTML Index Files/js/search.js
    Javascript functions for implementing
HTML Index Files/styles/myStyle.css
    style file for fileIndex.html
plotOne-IndexMaking.plot
    Plot file for time taken for indexing
plotTwo-SearchWord.plot
    Plot file for time taken to search a word
populateDict.py
    Creating dictionary of words, files, line nos
Optional
printToText.py
    Prints the index in a text file
Sample test directories ( 3 directories are present )
    153050049-15050050-Project/TestDirectories
```

## Functionality

This project indexes words in a directory. The indexed are shown in a HTML page, which not only provides the functionality of directly viewing the files in which the word is present, but also jumps to the required line number. We also provide the functionality of searching the HTML page for words, so that you need to scroll down the page to find it.

## Miscellaneous

To create index for your directory. Use the below code in any .py file and run it with python3.4
as mentioned above in Running section
Tested on Firefox 42.0
