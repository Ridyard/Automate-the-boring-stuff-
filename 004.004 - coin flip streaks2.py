#ATBS, chapter 4

# simulate n number of coin flips & record how many streaks occur

import random

results = []            # hold the simulated results of the coin flips
streak = 0              # how many n streaks encountered
currentRunningStreak = 0
cfSampleSize = 100       # user chosen, how many coin flips to sample
cfStreak = 6        # user chosen, no of matching flips that signifies a streak


## create sample of coin flips
for i in range(cfSampleSize):
    result = random.randint(0,1)
    if result == 0:
        results.append('T')
    else:
        results.append('H')
print(', '.join(results) + '\n')


## test for streaks
for result in range(len(results)):
    print('\ncurrent loop: ' + str(result))
    print('current count of matching results: ' + str(currentRunningStreak))

    print('current result is ' + str(results[result]))
    if currentRunningStreak < cfStreak:
        try:
            if results[result] == results[result+1]:        # see if element at i matches element at i+1 in results list
                print('>found sequential matching coin flips')
                if currentRunningStreak < cfStreak:     # if there are matching results & streak count hasn't been reached
                    print('>incrementing current running streak')
                    currentRunningStreak += 1
            else:
                print('>next result doesn\'t match the current result')  # if sequential flips don't match...
                currentRunningStreak = 0                                                        # resent running streak counter to 0
        except:
                print('end of list reached')    # results[result+1] on line 29 will eventually crash if not in a try / catch

                
    elif currentRunningStreak == cfStreak: # if streak is hit, increment streak counter & reset running counter
        print('streak hit, incrementing streak counter')
        streak += 1
        print('currentRunningStreak counter reset to 0')
        currentRunningStreak = 0

print('\nstreaks found: ' + str(streak))
print('chance of a streak: %s%%' % (streak / cfSampleSize * 100)) 



        
        

        
        
    



