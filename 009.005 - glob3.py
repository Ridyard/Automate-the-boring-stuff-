from pathlib import Path
import os

p = Path.cwd()
print(p)

# list all .py files in the cwd
q = list(p.glob('*.py'))
for i in q:
    print(i.name)


## create dict of the different file types in cwd

#create list of all entity names in cwd
count = {}
r = list(p.glob('*'))
for index, value in enumerate(r):
    r[index] = value.name    # ie 'spam.txt', .name refers to file name of a Path object
#print(r)

# add entity types to the dict based on file type
for i in r:    # for item in the list of file names+extensions in cwd
    #print(Path(i).suffix)
    count.setdefault(Path(i).suffix, 0)
    count[Path(i).suffix] += 1
count['sub-folder'] = count[''] # re name the empty suffix keys as 'sub folders'
del count[''] # then remove the '' key/values
print(count)
    



## create a txt file with the output of r
#path object methods only have basic functionality around files - should use open() with Path

s = Path('009.005 - output.txt')
s.write_text(str(count.items()))    # write-text() will overwrite the txt file, so in a for loop it will only write the last item in the loop
print(s.read_text())






