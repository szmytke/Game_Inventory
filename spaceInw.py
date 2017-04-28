import csv


def display_inventory(inventory):

    print('Inventory: ')
    for key, value in inventory.items():
        print(value, key)
    print('Total number of items: %d' % sum(inventory.values()))


def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        if added_items[i] not in inventory:
            inventory.update({added_items[i]: 0})
    for i in range(len(added_items)):
        for key in inventory:
            if key == added_items[i]:
                inventory[key] += 1
    return inventory


def print_table(inventory, order=None):
    # function sort and print element from inventory 

    print('Inventory: ')
    key_len_list = []                          # longest_str = max(len(key) for key in inventory)
    for key in inventory:                      #
        key_len_list += [len(key)]             #
    longest_str = max(key_len_list)            #
    print('  count%sitem name' % (' '*(longest_str-5)))
    print('----------------%s' % ('-'*(longest_str-5)))
    if order is None:
        for key, value in inventory.items():
            print('%7s' % value, key.rjust(8+(longest_str-5)))
        print('----------------%s' % ('-'*(longest_str-5)))
        print('Total number of items: %d' % sum(inventory.values()))
    if order == 'count,desc':
        par = []
        for key, value in inventory.items():
            par += [(value, key)]
        par.sort(reverse=True)
        for value, key in par:
            print('%7s' % value, key.rjust(8+(longest_str-5)))
        print('----------------%s' % ('-'*(longest_str-5)))
        print('Total number of items: %d' % sum(inventory.values()))
    if order == 'count,asc':
        par = []
        for key, value in inventory.items():
            par += [(value, key)]
        par.sort(reverse=False)
        for value, key in par:
            print('%7s' % value, key.rjust(8+(longest_str-5)))
        print('----------------%s' % ('-'*(longest_str-5)))
        print('Total number of items: %d' % sum(inventory.values()))


def import_inventory(inventory, filename='import_inventory.csv'):
    filecsv = open(filename, 'r')
    reader = csv.reader(filecsv)
    new_elem = []
    for row in reader:
        new_elem += row
    print(new_elem)
    add_to_inventory(inventory, new_elem)


def export_inventory(inventory, filename='export_inventory.csv'):
    filecsv = open(filename, 'w')
    writer = csv.writer(filecsv)
    elem_list = []
    for key, value in inventory.items():
        elem_list += [key]*value
    elem_list_text = ','.join(elem_list) + '\n'
    filecsv.write(elem_list_text)


def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragon_loot)
    import_inventory(inv)
    print_table(inv, 'count,desc')
    export_inventory(inv)


main()

