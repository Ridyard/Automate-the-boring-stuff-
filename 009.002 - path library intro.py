# atbs - path library

from pathlib import Path
import os

files = ['alex.txt', 'abby.csv', 'millie.docx']

for file in files:
    print(Path(r'C:\Users\Alex\Documents', file)) # not the best solution

print('================\n\n')

homefolder = Path('C:/Users/Alex/Documents') # because we're on windows, Path will amend the / to \
subfolder = Path('workspace')

print('1. ' + str(homefolder/subfolder)) # using / like this joins paths, and is a better solution than the join method (only for paths)

# / replaces the older os.path.join() mehtod

print('================\n\n')

print('2. current working directory is ' + str(os.getcwd()))
cwd = Path.cwd()
print(cwd)
print(Path.cwd())

home = Path.home()
print(home)

print('================\n\n')

print(Path('spam')/'bacon') # / needs to be used on a leftmost Path object; Path('spam') & cwd both refer to Path objects
print(cwd/'bacon')






