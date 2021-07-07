# atbs - chapter 10

# walk directory tree 2

import os
from pathlib import Path

#p = Path('C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39\\Workspace')
p = Path('C:\\Users\\Alex\\Documents\\Details')

for root, subfolders, files in os.walk(p):
    print(f'current folder is {root}')
    for subfolder in subfolders:
        print(f'\tsubfolder of {root}: {subfolder}')
    for file in files:
        print(f'\tfile inside {root}: {file}')



# aim is to print all files in workspace, excluding .git hidden files
#solution not currently working
p = Path('C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39\\Workspace\\ATBS')

for root, subfolders, files in os.walk(p):
    print(f'current folder is {root}')
    for subfolder in subfolders:
        i = Path(subfolder)
        j = []
        if i.glob('*.git*'):
            continue
        else:
            j.append(i)
        for item in j:
            print(item)

            
