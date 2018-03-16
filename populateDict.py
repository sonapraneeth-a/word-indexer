import sys
import copy
import re
import functools

'''
function to remove trailing apostrophe and apostrophe s.
'''
def removeapostrophes(x) :
    if x.endswith("\'s") :
        return x[0:len(x)-2]
    else :
        return x

'''
Function to remove HTML Tags
input :
    line : the line (or subline) to remove HTML tags from
    isWithingTag : represents whether the line was already inside a tag before it began
    level : the depth of the stack at this recursion point. Used for debugging purpose
'''
def removeHTMLTags(line, iswithintag, level) :
    #These are the HTML tags which will be removed
    f = open("tagList", "r")
    taglist=[]
    for lines in f:
        taglist.append(lines[:-1])
    actualtaglist=list(set(taglist))  # remove duplicate tags
    if iswithintag :
        if line.find(">") >=0 :    # continue from the index where the tag closes
            #print(line + "!!!")
            line=line.split(">",1)[1]
        else:
            return True," "        # if the tag does not close, indicate that the line is still inside the tag. Return an empty string to signify that the line has no words.

    #Here the line is not within a tag at the start
    linecopy = line
    returnline=""
    iswithintag=False
    #print("here" + line)
    if linecopy.find("<") == -1:   # if a tag doesnt start in the line, return back the whole line
        #print("here2" +" " + line)
        return False,line

	# else recursively remove tags
    while linecopy.find("<") >=0 :
        returnline=returnline+linecopy[0:linecopy.find("<")]
        linecopy = linecopy[linecopy.find("<")+1:len(linecopy)]
        #print(findfirstword(linecopy))
        if findfirstword(linecopy) in actualtaglist:
            iswithintag,remainingline=removeHTMLTags(linecopy,True,level+1)
            returnline=returnline+remainingline
            break
    #print("here22"+" "+returnline)
    return iswithintag,returnline

'''
Function which returns the first word in the tag.
'''
def findfirstword(linestring) :
    lines = linestring.strip("/").strip(" ");  # tag names can have a / at the beginning. Strip that.
    #print("blah" +lines)
    return lines.split(" ")[0].split(">")[0].upper() # return the first word in the tag

'''
Function which returns a list of words present in the line after processing special characters.
'''
def parseword(fileline):
    not_required_punctuations=["!","`","@","#","\$","%","\^","&","\*","\(","\)","\"",";",":","\?","\.","<",">",",","/","\{","\}","\[","\]","\|","-","\+","_","=","\\\\","\\t"]
    split_line=fileline.split(" ");
    split_words=[]
    for word in split_line :
        word_list=[word]
        #word_list=re.split("!|@|#|$|%|^|&|\*|(|)|\"|;|:|\?|\.|\<|\>|,|/|\{|\}|[|]|\||\\|-|\+|_|=",word)
        for punct in not_required_punctuations:
            #word_list=word_list+word.split(punct)
            word_list=functools.reduce(lambda x,y : x+y,list(map(lambda x : re.split(punct,x),word_list)))  # remove punctuations one by one
        split_words= split_words + word_list;
    split_words = list(filter(lambda x: x.strip() != "",split_words)) # remove empty words
    split_words = list(map(lambda x: x.strip("\'").lower(),split_words))
    split_words = list(map(lambda x: removeapostrophes(x),split_words)) # remove apostrophes
    split_words = list(filter(lambda x: not re.match("^[0-9]*$",x),split_words)) # remove "numerical" words
    return split_words

'''
Function to remove stop words from the dictionary
'''

def removeStopWords(word_dict) :
    return_dict = copy.deepcopy(word_dict)
    f = open ("ignoreWords","r")
    stopwordlist=set()
    for lines in f:
        if not lines.startswith("#") :
            stopwordlist.add(lines.strip())
    for key in word_dict.keys():
        if key in stopwordlist :
            del return_dict[key]
    return return_dict

'''
Main function : returns a dictionary of words indexed by file names given a set of files
'''

def populateDict(l) :
    word_dict = {}
    for files in l[0]:
        line_number=1
        file = open(files,"r")
        for line in file:
            words = parseword(line.strip())       #parse the line to give a list of words in the line
            for word in words:
                word_indexes = word_dict.get(word,{})
                file_index = word_indexes.get(files,[])
                file_index.append(line_number)
                word_indexes[files] = file_index
                word_dict[word] = word_indexes
            line_number += 1


    for files in l[1]:
        line_number=1
        file = open(files,"r")
        isWithinTag=False
        for line in file:
            isWithinTag,line1=removeHTMLTags(line.strip(), isWithinTag,0)
            words = parseword(line1.strip())       #parse the line to give a list of words in the line
            for word in words:
                word_indexes = word_dict.get(word,{})
                file_index = word_indexes.get(files,[])
                file_index.append(line_number)
                word_indexes[files] = file_index
                word_dict[word] = word_indexes
            line_number += 1

    word_dict = removeStopWords(word_dict)
    # print(word_dict)
    for key in word_dict.keys() :
        value = word_dict[key]
        word_dict[key]=list(map(lambda x:[x,value[x]],(sorted(value, key=lambda k: len(value[k]), reverse=True)))) #order by filename by frequency
        value = word_dict[key]
        word_dict[key]=list(map(lambda x: [x[0],sorted(list(set(x[1])))],value)) #remove duplicates and order line numbers in ascending order
        #print(word_dict)
    if 'nbsp' in word_dict:
        del word_dict['nbsp']  #nbsp is not a words
	#print(word_dict.get("listening","lol"))
    word_dict=list(map(lambda x:[x,word_dict[x]],(sorted(word_dict.keys(), key=lambda k: k, reverse=False)))) #sort based on word to create index
    #print(word_dict)
    return word_dict

#populateDict([[],['Siddharth\'s Homepage.html']])
