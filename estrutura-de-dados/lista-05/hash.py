class Item:

    def __init__(self, data) -> None:
        self.data = data

class Hash:
    def __init__(self, items, m, n) -> None:
        self.items = items # array of Item
        self.m = m # indice m is table size
        self.n = n # indice n is how records are currently in the table

def create_hash(m: int):
    created_hash = Hash(items={}, m=m, n=0)

    for i in range(0, created_hash.m):
        created_hash.items[i] = Item(data=None)

    return created_hash

def h(hash_table: Hash, data):
    return data % 7

def really_huge_h(hash_table: Hash, data, i):
    return (h(hash_table, data) + i) % hash_table.m

def search_hash(hash_table: Hash, data: int):
    i = 0
    do = True
    while do:
        address = really_huge_h(hash_table, data, i)
        if hash_table.items[address].data == data:
            return address
        i += 1

        if(i > hash_table.m or hash_table.items[address] is None):
            do = False
    return None

def insert_hash(hash_table: Hash, data: int):
    i = 0
    do = True
    while do:
        address = transforme(hash_table, data, i)
        if search_hash(hash_table, address) is None:
            hash_table.items[address] = Item(data=data)
            print(f'inserting in addres {address} the data {data}')
            hash_table.n += 1
            return True
        i += 1

        if(i > hash_table.m or hash_table.items[address] == data):
            do = False
    return True

def remove_hash(hash_table: Hash, data: int):
    if search_hash(hash_table, data) is None:
        return False
    hash_table.items[data] = Item(data=None)
    hash_table.n -= 1
    return True

def transforme(hash_table: Hash, data: int, transformed_data: int = None):
    if transformed_data:
        return transformed_data & hash_table.m
    return data % hash_table.m

def convert_data(data, rate):
    k = 0
    size_data = len(data)
    for i in range(0, size_data):
        k+= ord(data) * rate

    return k    

if __name__ == '__main__':
    hash_table = create_hash(13)
    name = 'MATEUSMACHAD'
    rate = 10
    for i in name:
        insert_hash(hash_table, convert_data(i, rate))
    print('------------')
    for i in range(13):
        data = hash_table.items[i].data
        if data:
            data_formated = chr(int(data/10))
        print(f'|{i} | {data_formated} was stored as {data}')
        data_formated = None
    print('---------')
    