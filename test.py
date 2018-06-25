import os
from pathlib import Path

s = 'test-dirs\\TestDirectories\\textDirectory\\lec19.txt'
s1 = 'test-dirs/TestDirectories/textDirectory/lec19.txt'
print(s.split('\\'))
r = "/".join(s.split('\\'))
r1 = "/".join(s1.split('\\'))
print("r: ", r)
print("r1: ", r1)

relativeFilePath = os.path.relpath(r, '.')
normRelativeFilePath = os.path.normpath(relativeFilePath)

print(relativeFilePath)
print(normRelativeFilePath)

