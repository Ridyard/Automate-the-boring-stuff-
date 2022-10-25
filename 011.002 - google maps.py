#! python3

# atbs - open google maps to a given address, taken from the clip board or cmd arguments

import webbrowser, sys, pyperclip

if len(sys.argv) >1: # if an argument is provided; sys.argv stores a list of prog's filename & arguments 
    address = ' '.join(sys.argv[1:]) #get addr from cmd, ignoring first argument (as this is the file itself)
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

