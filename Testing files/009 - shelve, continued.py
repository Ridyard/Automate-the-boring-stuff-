# atbs - this case is linked to 009 - shelve.py

import shelve

s = shelve.open('mydata')
print(s['dogs'])
s.close()

# references the .dat & .dir files
