# ATBS chapter 10 - basic shutil usage

import os, shutil
from pathlib import Path

os.chdir('testing files\\shutil test src') # make the cwd my testing directory
p = Path.cwd()

try:
    shutil.copy(p/'test1.txt', '..\\shutil test dest')  # copy txt doc from 1 folder to another
    shutil.copytree(p,'..\\shutil test dest')   # copy sub folders
except:
    print('may have encountered an issue')
