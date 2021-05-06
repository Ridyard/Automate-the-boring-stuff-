# atbs - saving with shelve

# binary shelf files

import shelve

sf = shelve.open('mydata')
dogs = ['millie', 'lulu', 'frank', 'kip']
sf['dogs'] = dogs
sf.close
# creates .dat & .dir files in cwd

##s = shelve.open('mydata')
##print(s['dogs'])
# added these lines to another file in the cwd to test the shelve module
