
# atbs - reading & writing files
# test of the path, glob & os modules

import os
from pathlib import Path
from pprint import pprint

p = Path.cwd()
print(p)

print('current running script - ' + os.path.basename(__file__) + '\n')

for i in p.glob('*.py'):    # glob() acts like a regex on filepaths / path objects - return all objects that end with '.py'
    print(os.path.basename(i))      # use the os module to prit just the path object base names

thisFile = open('009.008 - general module tests.py')
m = thisFile.readlines()  # returns a list of lines in the file object
for i in m:
    print('\t' + i)


