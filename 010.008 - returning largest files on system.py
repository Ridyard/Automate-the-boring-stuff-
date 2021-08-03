# atbs - chapter 10

##Write a program that walks through a folder tree and searches for exceptionally large files
##or folders—say, ones that have a file size of more than 100MB. (Remember that to get a
##file’s size, you can use os.path.getsize() from the os module.) Print these files with their
##absolute path to the screen.

import os, shutil
from pathlib import Path

home = Path.home()
print(home)

biggies = [] # to hold large files
errors = [] # to hold misc error files

for root, subs, files in os.walk(home): # walk the home directory
    for file in files:
        path_file = os.path.join(root, file) # this is used when traversing subfolders
        try:    
            if os.path.getsize(path_file) > 1024**3: # get all files greater than a gig in size
                biggies.append(file)
        except:
            errors.append(path_file) # error logging; certain misc file types will cause the script to crash


print(f'files within {home}, with a file size > 1GB:')
for i in biggies:
    print('\t' + i)

print(f'script encountered {len(errors)} path(s) that either did not exist or were unaccessible')
