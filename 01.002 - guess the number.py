# atbs, pg 22

#guess my age

myAge = 31
print('guess my age...\n')

a = True
while a == True:
    print('how old do you think i am?')
    guess = input()
    if int(guess) == myAge:
        print('correct!')
        a = False
    elif int(guess) > myAge:
            print('too high...')
    elif int(guess) < myAge:
        print('too low...')

