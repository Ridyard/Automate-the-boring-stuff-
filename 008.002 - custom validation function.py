# atbs - py input plus module
# input vaidation, does the input string add up to 10
# passing a custom validation function to inputCustom()

import pyinputplus as p     # import as whatever you want, pyip, p etc

def totalx(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('the digits must add up to 10, not %s' %(sum(numbersList)))
    return int(numbers)     # return numbers as an int if they do total 10
        


response = p.inputCustom(totalx)     # no parenthesis used for function call

