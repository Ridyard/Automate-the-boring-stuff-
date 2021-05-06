# atbs - files

from pathlib import Path
#import os


def read():
    f = open(Path.cwd()/ 'Testing files' / 'alex.txt', 'r') # look for alex.txt in sub folder of cwd
    # f is a file object; represents the txt file / 'a' mean append
    text = f.read()    # this prints the content of the file object 
    print(text)
    f.close()

read()

f = open(Path.cwd()/ 'Testing files' /'alex.txt', 'r') 
text = f.readlines()     # returns a list of txt split by \n
print(text)
f.close()

f = open(Path.cwd() / 'Testing files' /'alex.txt', 'a')
add = input('add text to alex.txt...')
f.write('\n' + add)
f.close()

read()


