

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.collisions = 0

        # '''
        # Research and implement the djb2 hash function
        # '''


def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        # check if key is already in the LL
        c_value = hash_table.storage[index]
        while c_value is not None:
            if c_value.key == key:
                # updated the c_value of a key that matches a key already there
                c_value.value = value
                return None
            c_value = c_value.next
        if c_value is None:
            # COLLISION
            hash_table.collisions += 1
            # We didn't return out so we didn't find an exisiting value to update.
            newPair = LinkedPair(key, value)
            newPair.next = hash_table.storage[index]
            hash_table.storage[index] = newPair
    else:
        # set the base value
        hash_table.storage[index] = LinkedPair(key, value)

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    c_value = hash_table.storage[index]
    p_value = hash_table.storage[index]
    if c_value is not None:
        while c_value is not None:
            if c_value.key == key:
                # Check if we're at the base node
                if c_value is hash_table.storage[index]:
                    # If there is only one here
                    if c_value.next is None:
                        # remove
                        hash_table.storage[index] = None
                        return None
                    else:
                        # more than one node?
                        # Set the base node to the next node
                        hash_table.storage[index] = hash_table.storage[index].next
                        return None
                else:
                    # If c_value isn't the base
                    # do we have a next one?
                    if c_value.next is not None:
                        # c_value is in between nodes in the list
                        # Update p_value to the next node & deleting c_value
                        p_value.next = c_value.next
                        return None
                    else:
                        # last node so we just set p_value.next to none
                        p_value.next = None
                        return None

            # p_value will only be the c_value the first time thru
            p_value = c_value
            # the rest will have the p_value be the last node we checked
            c_value = c_value.next
    if c_value is None:
        print(f'No key: {key} in the hash table.')
        return 1


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    c_value = hash_table.storage[index]
    if c_value is not None:
        while c_value is not None:
            if c_value.key == key:
                # if they keys are matching return the value
                return c_value.value
            c_value = c_value.next
    if c_value is None:
        # no matches
        return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_hash_table = HashTable(hash_table.capacity * 2)
    for i in range(0, len(hash_table.storage)):
        c_value = hash_table.storage[i]
        while c_value is not None:
            hash_table_insert(new_hash_table, c_value.key, c_value.value)
            c_value = c_value.next

    return new_hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity) +
          " to " + str(new_capacity) + ".")


Testing()
