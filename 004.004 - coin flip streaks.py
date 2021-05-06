# ATBS, chapter 4 - lists

## TO DO: currently records number of sequential matching pairs
## need to ensure it works correctly with greater numbers
## need to record matching pairs of head & tails

# record the number of heads & tails in 100 coin flips
# record how often a streak of 6 heads or tails occurs

import random

results = [] # results or coin tosses - H or T
streak = 0 # streak of matching pairs
count = 0 # running total of matchin pairs (will be incremented upon finding a match in the for loop & will revert to 0 after each iteration through the loop
inc = 1
streakMax = 3

# represents x coin flips
for i in range(10):
    coin = random.randint(0,1)
    if coin == 0:
        results.append('T')
    else:
        results.append('H')
print(', '.join(results))



for i in range(len(results)):
    currResult = results[i]
    print('\ncurrent loop is ' + str(i))
    print('current count is ' + str(count))
    print('current result is ' + results[i])
    try:
        print('next result in the results list is ' + results[i+1])
    except:
        print('\nend of results')

    
    if currResult == results[i+inc]:
        print('current result matches the next result')
        count += 1
        if count == streakMax-1: # if streak is hit, update streak counter and reset the running count to 0
            streak += 1
            print('streak hit, running count re-set to 0')
            print('running streak count ' + str(streak))
            count = 0
            continue            
    else:
        print('current result does not match the next result')
    continue

        
print('streaks of same results: ' + str(streak))



