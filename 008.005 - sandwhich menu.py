# atbs - sandwich menu

import pyinputplus as pyip

breads = {'wheat': 1.00, 'white': 0.95, 'sourdough': 1.10}
filling = {'chicken': 1.00, 'turkey': 1.25, 'ham': 1.10, 'tofu': 0.95}
cheese = {'cheddar': 0.50, 'swiss': 0.90, 'mozzarella': 0.80}
extra = {'mayo': 0.25, 'mustard': 0.25, 'lettuce': 0.55, 'tomato': 0.75}
order = []

print('===============')
print('sandwhich menu')
print('===============\n')


while True:
    b,f,c,e = '', '', '', ''
    
    b = pyip.inputMenu(['wheat', 'white', 'sourdough'])
    f = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
    if pyip.inputYesNo('add cheese?') == 'yes':
        c = pyip.inputMenu(['cheddar', 'swiss', 'mozarella'])
    if pyip.inputYesNo('extras?') == 'yes':
        e = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])

    print('\nreview sandwhich:')
    print('%s on %s bread' % (f, b), end='')
    if c or e:
        print(' with ', end='')
    if c:
        print(c, end='')
    if c and e:
        print(' and ', end = '')
    if e:
        print(e)

    order.append([b,f,c,e])

    add = pyip.inputYesNo('\nadd another sandwhich to order?')
    if add == 'no':
        break
print(order)



''' to do
add cost total - use classes for this
add recrsive call to print list, list items'''
    
