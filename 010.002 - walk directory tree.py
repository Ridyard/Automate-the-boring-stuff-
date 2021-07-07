# ATBS - chapter 10
# walking a directory tree

import os
from pathlib import Path

p = Path('C:\\Users\\Alex\\Pictures')
#p = Path('C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39\\Workspace')
print(p)
for folderName, subfolders, filenames in os.walk(p):
    print(f'current folder is {folderName}')
    for subfolder in subfolders:
        print(f'\tsubfolder of {folderName}: {subfolder}')
    for filename in filenames:
        print(f'file inside {folderName} {filename}')
    print('')


