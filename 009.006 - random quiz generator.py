#
# random quiz generator

import random, os
from pathlib import Path

guitarists = {'led zeppelin' : 'Jimmy Page', 'pearl jam' : 'mike mccready', 'band of gypsies' : 'jimi hendrix',
              'black sabbath' : 'tony iommi', 'the police' : 'andy summers', 'the hives' : 'vigilante carlstrom',
              'acdc' : 'angus young', 'metallica' : 'kirk hammett', 'aerosmith' : 'joe perry', 'sum 41' : 'derek whibly',
              'the strokes': 'albert hammond jr', 'the stooges' : 'ron ashton', 'smashing pumpkins' : 'billy corgan',
              'cream' : 'eric clapton', 'RHCP' : 'john frusciante', 'QOTSA' : 'josh homme',
              'black label society' : 'zakk wylde', 'the mars volta' : 'omar rodriguez lopez', 'EODM' : 'jesse hughes',
              'guns n roses' : 'slash', 'the raconteurs' : 'brendan benson', 'pink floyd' : 'dave gilmore'}

print(len(guitarists))
print('guess the guitarist of a given band\n')

for quizNum in range(5):
    q = open(Path.cwd() / 'Testing files' / 'random quiz generator'/ ('guitaristQuiz'+ str(quizNum + 1) + '.txt'), 'w')
    a = open(Path.cwd() / 'Testing files' / 'random quiz generator' / ('guitaristAnswers' + str(quizNum + 1) + '.txt'), 'w')

    q.write('name:\ndate:\n\nguess the guitarist of each band\n\n')
    bands = list(guitarists.keys()) # make a list of bands from guitarists dict keys
    random.shuffle(bands)

    for questionNum in range(len(guitarists.keys())):
        correctAns = guitarists[bands[questionNum]] # picks the i band from the shuffled bands list, uses this as a key in guitarists dict
        wrongAns = list(guitarists.values())
        wrongAns.remove(correctAns) # remove the correct answer from the list of bands
        wrongAns = random.sample(wrongAns, 3) # pick 3 random bands as wrong answers
        answerOptions = [correctAns] + wrongAns # create a list of 1x correct & 3x incorrect answers
        random.shuffle(answerOptions)

        # write question & answerOptions to question files
        q.write(f"{questionNum + 1}. who is the guitarist in {bands[questionNum]}?\n") # using f string rather than %
        for i in range(4):
            q.write(f"\t{'ABCD'[i]}.{answerOptions[i]}\n")
        q.write('\n')

        #write answer key to file
        a.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAns)]}. {correctAns}\n")
    q.close()
    a.close()
print('complete')

        
        
    
    





    
##    q = open(Path(cwd)/'Testing files' / 'random quiz generator'/ ('quizNum' + str(quizNum + 1) + '.txt'), 'w')
##    #a = open(
##    print('question ' + str(quizNum+1) + ':')
##    print('who was the guitarist in ' + BANDNAME)
##    choice = input()
##    if choice == guitarists[BANDNAME]:
##        score += 1
