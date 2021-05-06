# atbs, Chapter 3

# magic 8 ball

import random

def getAnswer(numberIn):
    if numberIn == 1:
        return 'it is certain'
    elif numberIn == 2:
        return 'it is dceidedly so'
    elif numberIn == 3:
        return 'yes'
    elif numberIn == 4:
        return 'reply hazy, please try again'
    elif numberIn == 5:
        return 'outlook not so good'
    elif numberIn == 6:
        return 'no'
    elif numberIn == 7:
        return 'doubtful'
    elif numberIn == 8:
        return 'maybe baby'

#r = random.randint(1,8) # random number between & including 1-8
#fortune = getAnswer(r)
#print(fortune)

print(getAnswer(random.randint(1,8))) # the above lines evaluate to this...
