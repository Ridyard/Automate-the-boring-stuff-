import os, random
from pathlib import Path


## second / solo attempt at random quiz generator from ATBS

guitarists = {'led zeppelin' : 'Jimmy Page', 'pearl jam' : 'mike mccready', 'band of gypsies' : 'jimi hendrix',
              'black sabbath' : 'tony iommi', 'the police' : 'andy summers', 'the hives' : 'vigilante carlstrom',
              'acdc' : 'angus young', 'metallica' : 'kirk hammett', 'aerosmith' : 'joe perry', 'sum 41' : 'derek whibly',
              'the strokes': 'albert hammond jr', 'the stooges' : 'ron ashton', 'smashing pumpkins' : 'billy corgan',
              'cream' : 'eric clapton', 'RHCP' : 'john frusciante', 'QOTSA' : 'josh homme',
              'black label society' : 'zakk wylde', 'the mars volta' : 'omar rodriguez lopez', 'EODM' : 'jesse hughes',
              'guns n roses' : 'slash', 'the raconteurs' : 'brendan benson', 'pink floyd' : 'dave gilmore'}

## create & change to relevant quiz directory
p = Path.cwd()
try:
    os.mkdir(p/'testing files\\random quiz generator 2')
except:
    (' ')
os.chdir(p/'testing files\\random quiz generator 2')


## create quiz files
for i in range(5):

    ## get list of dict keys
    quizKeys = list(guitarists.keys())
    
    q = open(f'quiz {i+1}.txt', 'w')
    a = open(f'answers {i+1}.txt', 'w')
    q.write(f'guitarist quiz {i+1}\nmatch the guitarist to the band:\n\n')
    
    for j in range(4): # 4 questions per quiz
        for k in range(4): # 4 quiz options
            quizOptions = random.sample(quizKeys, 4)
        for l in quizOptions:
                q.write(f'- {str(l)}\n')
        
        tempOption = guitarists[quizOptions[random.randint(0, len(quizOptions)-1)]] # pick random guitarist from quizOptions as the answer option
        q.write(f'\n {tempOption} \n\n\n')
        for k, v in guitarists.items():     # remove the guitarist so that it can't be used in another question in the l quiz file
            if v == tempOption:
                a.write('- ' + tempOption.upper() + ' is in ' + k.upper() + '\n') # write the answer option to file before removing it from quizKeys
                quizKeys.remove(k)
    q.close()
    a.close()















    
