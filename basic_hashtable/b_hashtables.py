

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''


def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return hash % max


print(hash("Mia", 11))
print(hash("Tim", 11))
print(hash("Chase", 11))
print(hash("Jan", 11))


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        print(f"Collision: {key} / {hash_table.storage[index].key}")
    hash_table.storage[index] = Pair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hash_key = hash(key, hash_table.capacity)
    index = hash_key % hash_table.capacity
    if hash_table.storage[index] != None:
        hash_table.storage[index] = None
    else:
        print(f"Hash Table does not contain {key}")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        return None
    return hash_table.storage[index].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
