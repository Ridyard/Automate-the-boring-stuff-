# atbs - returning a list of the largest files on the system

import os
from pathlib import Path

biggies = {} # to capture the large files in a given directory
p = Path('C:\\Users\\alexa\\Pictures')

for folder, subs, files in os.walk(p): # walk through target directory
    for file in files:
        print(folder)
        print(file)
        
        os.chdir(folder) # changing to the target directory to walk       
        try:
            size = os.path.getsize(file)
            print(f'{size} bytes\n')

            if size > 1048576: # if file is a >mb 
                biggies[file] = round(size/1048576,2) # standardize the file format to mb and add to dict

        except Exception as err:
            print(str(err) + '\n')

print('==========================================')
print('==========================================')

print(f'\nlargest files in {p}:\n\n')

biggest = {} # to hold the top 10 biggest files
for i in range(10):
    b = max(biggies, key=biggies.get)
    biggest[b] = biggies[b]
    biggies.pop(b) # add the largest file from biggies to biggest dict; remove this from biggies; repeat


sortedBiggest = dict(sorted(biggest.items(), key=lambda item: item[1], reverse=True)) # sort bigges items by size

for k,v in sortedBiggest.items():
    print(f'-\t{k}:\n\t{v}mb')


