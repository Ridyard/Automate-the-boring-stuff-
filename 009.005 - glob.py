# atbs - glob

from pathlib import Path
import os

cwd = Path.cwd()
print('files in ' + str(cwd))

for i in cwd.glob('*'):  # lists all files in the directory
    print(i)

# print(list(cwd.glob('*')))

for i in cwd.glob('*.txt'): # parameter allows only .txt files to be returned; glob works similar to regex
    print(i)

print('\nall .py scripts from this chapter:')
for i in cwd.glob('009*'):
    print(i)

# glob() returns a generator object
