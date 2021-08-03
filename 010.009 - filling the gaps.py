# atbs - chapter 10

##Filling in the Gaps
##
##Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on,
##in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and
##spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.
##
##As an added challenge, write another program that can insert gaps into numbered files so that a
##new file can be added.


import os, shutil, re
from pathlib import Path


p = Path.cwd()/'testing files/backupToZip' # navigate to test folder where txt files are stored
dirFiles = [] # to hold spamfile paths

for i in p.glob('spam?.txt'):
    dirFiles.append(str(i)) # convert windows path object to a str for use later on
spamString = ', '.join(dirFiles)
#print(spamString)

f = re.compile(r'''(
    ([C]:\\                                # starts with C:
    [a-zA-Z0-9\_\\,\s]+        # filepath
    spam)                            # spam filename
    (\d+)                                 # number
    (.txt)
    )''',re.VERBOSE)        # brackets indicate groups

mo = f.findall(spamString) # list to contain the match objects
newSpamFiles = [] # to contain correct indexed spamfiles



''' this block identifies any gaps in numbering and creates a clensed list
of file paths'''
for index, value in enumerate(mo):
    print(value[1],value[2], value[3]) # get file path (including spam), spam-number & .txt parts
    if index != int(value[2]): # identify gap in sequential numbering
        print('break in naming convention - generatng new file name...')
        value = ''.join([value[1], str(index), value[3]]) # if non-sequential spam number found, then rename
        newSpamFiles.append(value)
    else:
        newSpamFiles.append(value[0])
        
print('\n')
for i in newSpamFiles:
    print(i)

print('\ndirFiles')
for i,v  in enumerate(dirFiles):
    print(v)
    shutil.move(dirFiles[i], newSpamFiles[i])
print('done')


## to do: make script work with files spam>9





# -------------------------------------------
# # this will return missing elements from a list of numbers; NOT USED BUT HANDY FOR FUTURE

##def missingElements(L):

##    start, end = L[0], L[-1]
##    return set(range(start, end+1)).difference(L)

##lst = [0, 1, 3, 4, 6]
##x = missingElements(lst)
##print(x)
    
# --------------------------------------------







    
