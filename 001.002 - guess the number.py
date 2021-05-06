# atbs, pg 22

#guess my age


import random

myAge = random.randint(1,100) # returns a random int between 1-100
print('guess my age...\n')



def hint1():
    if myAge %2 == 0:
        print('\nthe number is even')
    else:
        print('\nthe number is odd')
    print('*type "hint" for more hints...\n')

def hint2():
    print('\nthe number is between ' + str(myAge - random.randint(1,15)) + ' & ' + str(myAge + random.randint(1,15)) + '\n')

def hint3():
    closest = min(guesses, key=lambda x:abs(x-int(myAge))) # not sure what lambdas do yet / this line returns the current closest guess as an int
    print('your closest guess was ' + str(closest))
    


hint = 0
count = 0
a = True
guesses = []

while a == True:
    if count == 5:
        hint += 1
        hint1() # provide a hint if user is struggling

    print('how old do you think i am?')
    guess = input()
    if guess == 'hint':
        if hint >= 2:
            hint3()
        else:
            hint2() # user needs another hint
        hint += 1
        
    elif int(guess) == myAge:
        print('correct!')
        count += 1
        a = False
        
    elif int(guess) > myAge:
        print('too high...')
        count += 1
        guesses.append(int(guess)) # convert guess to int & add to list for use by hint functions
        
    elif int(guess) < myAge:
        print('too low...')
        count += 1
        guesses.append(int(guess))
     
print('you guessed in ' + str(count) + ' attempts')
if hint: # if hint evaluates to True / >0
    print('you used ' + str(hint) + ' hints')

