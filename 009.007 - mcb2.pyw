#! python3

# atbs - multi-clipboard
# ver2 that incorporates the shelve module

# The command line argument for the keyword is checked.
# If the argument is save, then the clipboard contents are saved to the keyword.
# If the argument is list, then all the keywords are copied to the clipboard.
# Otherwise, the text for the keyword is copied to the clipboard.

# usage: mcb.pyw <keyword>

import pyperclip, sys, shelve

mcbShelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:

mcbShelf.close()
