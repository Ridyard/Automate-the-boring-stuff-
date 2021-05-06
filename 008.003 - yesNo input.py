# atbs - pyinputplus

''' inputYesNo() will handle yes no, y n, YES NO, Yes No responses
 convenient way of handling / validating user input'''

import pyinputplus as pp

while True:
    prompt ='want to keep an idiot busy for hours?\n'
    response = pp.inputYesNo(prompt, yesVal='yup', noVal='nope') # passing args overrides what resonses are handled, remove these to go back to yesNo

    if response == 'no':
        break
