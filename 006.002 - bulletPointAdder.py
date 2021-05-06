#! python3
# atbs - manipulating strings

# get text from the clipboard, add a star and a space to the beginning of each line

import pyperclip, sys

text = pyperclip.paste()    # get text from clipboard as a list
text = text.split('\n')
print(text)
print()

for i in range(len(text)): 
    if text[i].isspace():   # if text contains a blank line then skip
        continue
    else:
        text[i] = '* ' + text[i]

text = '\n'.join(text)
print(text)

pyperclip.copy(text)
