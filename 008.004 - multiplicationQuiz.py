# atbs - multiplication quiz
"""10x random arithmetic questions using pyinputplus module"""

import random, time, pyinputplus as pyip

"""function that will present the math question, record answers & provide end-game output"""
def startQuiz(numQuestions, l, t, score):
    for i in range(numQuestions):
        a = random.randint(1,10)
        b = random.randint(1,10)
        prompt = (f"\nwhat is {a} x {b}? ")
        responseTime = 0
        
        try:
            start = time.time() # start recording user response time
            
            answer = pyip.inputStr(prompt, allowRegexes=['^%s$' % (a*b)],
                                    blockRegexes=[('.*', 'incorrect!')], 
                                    timeout=t, limit=l)

        except pyip.TimeoutException:
            print('out of time')
        except pyip.RetryLimitException:
            print('out of tries')
        else: # triggers if no exceptions were raised in try block
            print("correct!")
            score +=1 # increment the user score

        end = time.time() # stop recording user response time
        response = end - start
        responseTime += response
    
    # output block based on the user's end scoreline
    print(f"\nyou scored {score}/10!")
    responseTime = round(responseTime, 2)
    print(f"your average time per question was {responseTime} seconds")
    if score <5:
        print('better luck next time...\n')
    elif score >=5 and score <10:
        print('well done!\n')
    else:
        print('a perfect score\n!')



        
numQuestions = 10
difficulty = pyip.inputChoice(prompt="\nselect difficulty:", choices=['easy','medium','hard'])
score = 0 # to hold the overall scoreline

# update game criteria based in difficulty selected
# l = limit of guesses / t = time to guess (seconds)
if difficulty == 'easy':
    l = 10
    t = 10
elif difficulty == 'medium':
    l = 4
    t = 5
elif difficulty == 'hard':
    l = 1
    t = 3
startQuiz(numQuestions, l, t, score)





