#atbs - zip test

import zipfile, os
from pathlib import Path

p = Path.cwd()/'testing files/zip test'

zt = zipfile.ZipFile(p / 'zipper.zip')  # create zipfile object (zt)
print(zt.namelist()) # namelist returns the files within the zip folder

for i in zt.namelist():
    fileInfo = zt.getinfo(i)
    print(f'{i} size before compression {fileInfo.file_size}')
    print(f'{i} size after compression {fileInfo.compress_size}')
    print(f'compressed size is {round(fileInfo.file_size / fileInfo.compress_size,2)}x smaller!') # work out filesize / compress size and round to 2pd
    print()
    

print('=====================================================')
fileInfo = zt.getinfo('zipper.txt') # refer to specific file in zip file
print(f'fileInfo size (before compression) is {fileInfo.file_size}') # get size of the txt file that fileInfo object refers to
print(f'fileInfo size (after compression) is {fileInfo.compress_size}') # get compressed size of txt file

zt.close()  
