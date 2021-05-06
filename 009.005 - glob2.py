# atbs
# glob - list the contents of a folder according to a given pattern (think regex)

from pathlib import Path

print('cwd is ' + str(Path.cwd()))
p = Path.cwd()


# this function returns / prints all .py files in cwd
print('files in cwd:')
for i in p.glob('*.py'):  # glob object will return any file that ends in .py
    print(i.name)       # i.name (no brackets) will return the file name & extension


# this function returns / prints all files in cwd with a given file extension (ext)
print('\nenter a file extension to list the contents in cwd...')
ext = input()
if not ext.startswith('.'):     # check input validity; add preceding . if omitted
    ext = '.' + ext
for i in p.glob('*'+ext):
              print(i.name)
