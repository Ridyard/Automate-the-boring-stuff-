# atbs - fantasy game inventry

inv = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
loot = ['gold coin', 'gold coin', 'ruby', 'dragon scale', 'dragon scale', 'arrow']


def displayInventory(inv):
    itemTotal = 0
    print('inventory:')
    for k,v in inv.items():
        print(v,k)
        itemTotal += v
    print(f'total number of items {itemTotal} \n')


def addToInventory(inv, loot):
    for i in loot:
        inv.setdefault(i, 0) # if i not currently in inv, then we add & set default to 0
        inv[i] +=1           # we then increment
        print(f'collected {i}!')
    print()


displayInventory(inv)
addToInventory(inv, loot)
displayInventory(inv)
