import os
import copy
import time
import populateDict
import printHTMLList
import matplotlib.pyplot as plt
import mimetypes
import glob

files = glob.glob('./HTML Index Files/textDirectory/*.txt')

# files = ['./textDirectory/lec01.txt','./textDirectory/lec02.txt','./textDirectory/lec03.txt',
# 		'./textDirectory/lec04.txt','./textDirectory/lec05.txt','./textDirectory/lec06.txt',
# 		'./textDirectory/lec07.txt','./textDirectory/lec08.txt','./textDirectory/lec09.txt',
# 		'./textDirectory/lec10.txt','./textDirectory/lec11.txt','./textDirectory/lec12.txt',
# 		'./textDirectory/lec13.txt','./textDirectory/lec14.txt','./textDirectory/lec17.txt',
# 		'./textDirectory/lec16.txt','./textDirectory/lec18.txt','./textDirectory/lec19.txt',
# 		'./textDirectory/lec20.txt','./textDirectory/lec21.txt','./textDirectory/lec23.txt']

listFileSize = []
timeSize = []
listFileSizeString = []
timeSizeString = []
for txt in files:
	fileSize = os.path.getsize(txt)/1024
	newFiles = [[txt],[]]
	start_time = time.time()
	populateDict.populateDict(newFiles);
	populateDictTime = time.time() - start_time
	#print( 'Function populateDict ' , populateDictTime, 'sec for file size ', fileSize)
	listFileSizeString.append(str(fileSize))
	timeSizeString.append(str(populateDictTime))
	listFileSize.append(fileSize)
	timeSize.append(populateDictTime)

fileSizeSortedString = copy.deepcopy(listFileSizeString)
fileSizeSortedString.sort(key=float)
fileSizeIndex = [listFileSizeString.index(x) for x in fileSizeSortedString]
timeSorted = [timeSize[y] for y in fileSizeIndex]
fileSizeSorted = sorted(listFileSize)

#print(listFileSize)
#print(timeSize)

#plt.plot(listFileSize, timeSize)
#plt.show()

fileId = open('runningTimeIndexMaking.txt', 'w')
numLines = len(fileSizeSorted)
fileId.write('File Size')
fileId.write('\t')
fileId.write('Time')
fileId.write('\n')
for i in range(0,numLines):
	#fileId.write(str(fileSizeSorted[i]))
	#fileId.write(str(round(fileSizeSorted[i],2)))
	stringToWrite = str.format("{0:.3f}", fileSizeSorted[i])
	fileId.write(stringToWrite)
	fileId.write('\t')
	#fileId.write(str(timeSorted[i]))
	fileId.write(str(round(timeSorted[i],2)))
	fileId.write('\n')
fileId.close();

graph = plt.plot(fileSizeSorted, timeSorted)
plt.ylabel('Time(sec)')
plt.xlabel('File Size(kB)')
plt.setp(graph, linewidth=2.0, linestyle='-', color='b', label='Running Times')
points = plt.plot(fileSizeSorted, timeSorted, 'ro')
plt.title('Time for creating index vs File size')
#plt.show()
plt.grid(b=None, which='major', axis='both')
plt.savefig('runningTimeIndexMaking-Python.png', bbox_inches='tight')
plt.show()