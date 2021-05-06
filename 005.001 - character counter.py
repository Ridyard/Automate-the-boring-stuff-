# ATBS - Chapter 5

# Count the number of occurrances of each letter



import pprint

print('enter a line of text...')
text = input()
letters = {}

for i in text:
    i = i.lower()
    letters.setdefault(i, 0)
    letters[i] += 1

pprint.pprint(letters) # orders the keys / output
