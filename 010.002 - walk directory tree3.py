# atbs

import os, shutil
from pathlib import Path

p = Path('C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39\\Workspace\\ATBS')
l = []

for root, subs, files in os.walk(p):
    print(f'current directory is {root}')
    for sub in subs:
        print(f'\tsub folder within {root}: {sub}')
        
