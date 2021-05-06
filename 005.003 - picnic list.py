# ATBS - Chapter 5
# nested dictionaries

import pprint

# declare initial dict
picnicList = {'alex':{'bread':1, 'cheese':4, 'beer':20},
              'abby':{'olives':2, 'dip':4, 'crisps':3, 'gin':1, 'tonic':8},
              'david':{'crisps':2, 'chocolate':4, 'cakes':2, 'beer':10},
              'george':{'ham':3, 'chicken':3, 'cheese':3, 'rum':1, 'coke':2}}


# totals how many of each item will be brought accross multiple guests
def totalBrought(picnicList):
    totalItems = {}
    for k, v in picnicList.items(): # cycle through top level dict
        for k2, v2 in v.items(): # cycle through inner dicts
            totalItems.setdefault(k2, 0)
            totalItems[k2] += v2
            print(str(v2) + 'x ' + str(k2) + ' added')
    print()
    return totalItems    


# check how many of a given item will be brought to the picnic
def checkItems(picnic):
    print('enter a picnic item to see how many will be brought...')
    print('...leave blank to exit')
    while True:  
        check = input()
        if check != '':     
            if check in picnic:
                    print(str(picnic[check]) + 'x ' + check + ' being brought')
            else:
                    print(str(check) + ' not being brought by any guests to picnic')
        else:
            break


# add an item and/or guest to the picnic list
def add(picnicList):
    while True: 
        print('\nadd item to the picnic list... what item?')
        print('...leave blank to exit')
        item = input()
        if item == '':
            break
        else:
            print('how many?')
            qty = int(input())
            print('who is bringing the ' + item + '?')
            owner = input()

        if owner in picnicList:
            picnicList[owner].setdefault(item, 0)
            picnicList[owner][item] += qty
            print(str(qty) + 'x ' + item + ' added to ' + owner + '\'s list')
            pprint.pprint(picnicList)
        elif owner not in picnicList:
            picnicList[owner] = {item: qty} # add nested dict
            pprint.pprint(picnicList)
    return picnicList



picnic = totalBrought(picnicList)
print(str(len(picnic)) + ' unique items being brought to picnic\n')

print('==========')
print('picnic items')
print('==========')

print('enter \'view\' to check the full picnic list')
print('enter \'check\' to check how many of a given item will be brought to the picnic')
print('enter \'add\' to add another item to the picnic list')
print('leave blank to exit')
choice = input()

if choice == 'view':
    pprint.pprint(picnicList)
elif choice == 'check':
    checkItems(picnic)
elif choice == 'add':
    picnicList = add(picnicList)
elif choice == '':
    print()    






