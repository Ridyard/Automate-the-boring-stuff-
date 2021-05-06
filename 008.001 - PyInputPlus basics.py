# atbs - input validation
# pyinputplus basics

# third party module

import pyinputplus as pyip

##inputStr() Is like the built-in input() function but has the general PyInputPlus features.
##You can also pass a custom validation function to it

##inputNum() Ensures the user enters a number and returns an int or float, depending on
##if the number has a decimal point in it

##inputChoice() Ensures the user enters one of the provided choices

##inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options

##inputDatetime() Ensures the user enters a date and time

##inputYesNo() Ensures the user enters a “yes” or “no” response

##inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and returns a
##Boolean value

##inputEmail() Ensures the user enters a valid email address

##inputFilepath() Ensures the user enters a valid file path and filename, and can optionally check
##that a file with that name exists

##inputPassword() Is like the built-in input(), but displays * characters as the user types so that
##passwords, or other sensitive information, aren’t displayed on the screen












name = pyip.inputStr('enter your name...')

age = pyip.inputNum('enter your age...')
