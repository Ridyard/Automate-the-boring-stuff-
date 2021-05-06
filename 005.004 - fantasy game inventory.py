# atbs - practice project
# fantasy game inventory


def displayInvent(inventory):
    print('inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal += v
    print('total number of items: ' + str(itemTotal))

def addInvent(inventory, dragonLoot):
    addItems = {}
    for item in dragonLoot:     # add dragonLoot list items to a dict
        addItems.setdefault(item, 0)
        addItems[item] +=1
        print(item + ' collected')
    print(addItems)
    print()
    
    for k, v in addItems.items():   # add new dragonLoot dict items to existing inventory 
        inventory.setdefault(k, 0)
        inventory[k] += v
        print(str(v) + 'x ' + k + ' added to inventory')
    print(inventory)
    print()
    return inventory



inventory = {'dagger': 1, 'rope': 3, 'gold coin': 42, 'arrow': 12, 'torch': 3}
displayInvent(inventory)
print()

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addInvent(inventory, dragonLoot)
displayInvent(inv)        
