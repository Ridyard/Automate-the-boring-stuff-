# atbs - files

from pathlib import Path

c = Path.cwd()  # show where the txt file is saved
print(c)

p = Path.cwd() / 'read & write files' / 'alex.txt'
p.write_text('hello world')

text = p.read_text()
print(text)
