# atbs - working with directories
"""make use of different functions to work with directories"""

from pathlib import Path

print('this script will return a list of files of a given type')
filePath = input('enter file path or leave blank to use cwd...')
fileType = input('enter the file type...')

if fileType.startswith('.'): # remove any leading '.' from the filetype; standardise input
    fileType = fileType[1:]

if filePath == '':
    filePath = Path.cwd() # if file path is omitted, use cwd
else:
    filePath = Path(filePath) # otherwise use the user selected path

try:
    q = list(filePath.glob('*.' + fileType)) # glob will return items in cwd with the given fileType
    for i in q:
        print('> ', end='')
        print(Path(i).stem) # paths .stem method strips the parent / file path of the returned items, so we just print the file names for readability
except:
    print('error ocurred')

