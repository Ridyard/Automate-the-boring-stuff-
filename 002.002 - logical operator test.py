# atbs, pg 59

# practice question 9,

# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
# stored in spam, and prints Greetings! if anything else is stored in spam.


print('enter something...')
spam = input()

if spam == '1':
	print('hello')
elif spam == '2':
	print('howdy')
elif spam != '2' or spam != '3':
	print('greetings')
