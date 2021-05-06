# atbs - manipulating strings

# practice question 1

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

r1 = []

for i in tableData:
    for j in range(len(i)):
        r1.append(j[0])
print(r1)
