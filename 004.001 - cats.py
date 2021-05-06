# atbs

# lists

print('how many cats do you have?')
nCats = int(input())

cats = []

for i in range(int(nCats)):
    print('enter the name of cat #' + str(i+1))
    cat = input()
    cats += [cat]


# loop 1
print(' the cat names are ')
for i in cats:
    print(i)

    
# loop 2
for i in range(len(cats)):
    print('index ' + str(i) + ' in cats is ' + cats[i])


# loop 1 and 2 function in a similar way
# using range(len(listName) is handy because the code in the loop can access the index (as the
# variable i) and the value at the index (as cats[i])


for index, item in enumerate(cats):
    print('index ' + str(index) + ' in the cat list is ' + str(item))

# loop 3 works in a similar way to loop 2
# on each iteration through the loop, enumerate will return the index of the item in the list & the item itself
