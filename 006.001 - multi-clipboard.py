#! python3
# atbs - manipulating strings

# multi-clipboard for automatic messages

import pyperclip, sys

text = {'agree' : """Yes, i agree. That sounds fine""",
        'busy' : """Sorry, can we do another time?""",
        'upsell' : """Would you consider making a monthly donation?"""}

# sys.arg is a list that should always contain command line arguments passed to the script
# contains a list of strings: the filename & command line argument
if len(sys.argv) < 2:
    print('the name of the program is ' + sys.argv[0])
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(text[keyphrase] + ' copied to clipboard')
else:
    print('there is no text associated with the phrase ' + keyphrase)
