items = {'rope':1,'torch':6,'gold coin':42,'dagger':1}

def displayInventory (inventory):
    print('Inventory: ')
    item_total = 0
    for item, amount in inventory.items():
        print (item, amount)
        item_total += amount
    print('Total items: '+str(item_total))

def lootItems(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item]=1

#example
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
lootItems(items, dragonLoot)
print (items)
