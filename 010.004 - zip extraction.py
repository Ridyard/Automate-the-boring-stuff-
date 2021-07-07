# atbs - zip extraction

import os, zipfile, send2trash, time
from pathlib import Path

p = Path.cwd()/'testing files' / 'zip test' / 'zip extraction destination'

ez = zipfile.ZipFile(p/'..'/'zipper.zip')
print(ez.namelist())

ez.extractall(p) # extract all files in zip to a given path (otherwise it would be extracted to cwd)




## aim is to check whether the ez.namelist() items are in the destination folder
try:    
    for i in os.listdir(p): # get contents of dest folder
        if i in ez.namelist():
            print(f'sucess: {i} has been extracted to dest folder')
except:
    print('error encountered')
print()


## send extracted files to trash and close file
time.sleep(10) # add a timed delay so that we can see extracted files before moving on to deletion code
for j in os.listdir(p):
    print(f'{j} has been deleted from the extraction destination folder')
    send2trash.send2trash(str(p/j)) # need to include the path to the desired file
    #os.unlink(p/'dog.txt')     # this is a permanent deletion

ez.close()
