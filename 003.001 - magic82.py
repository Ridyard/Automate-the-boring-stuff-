# atbs, chapter 4
# magic 8 ball with lists

import random

magic8 = ['yes', 'no', 'maybe', 'ask again', 'outlook not so good', 'outlook hazy', 'it is certain', 'doubtful']

print(random.choice(magic8))

# random.choice(magic8) is equivalent to magic8[random.randint(0,len(magic8)-1)]
