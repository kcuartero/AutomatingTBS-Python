#inventory.py
stuff = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger': 1 , 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, quantity in inventory.items(): #for loop through all key and value of the stuff dictionary
        print(str(quantity)+' '+item) # output quantity and the item name (ex. "1 rope")
        item_total += quantity # sum of quantity
    print("Total number of items: " + str(item_total))

displayInventory(stuff) 

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault (item,0) #if no value for key, then make it 0 by default
        inventory[item] += 1 # for each item that appears in dragonLoot, increase value by 1
    return inventory  

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin','gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)