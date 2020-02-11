# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table with `capacity` buckets that accepts string keys.
    storage: internal array that stores each inserted value in a 
    `bucket` based on key provided
    '''

    def __init__(self, capacity):
        self.capacity = capacity  
        self.storage = [None] * capacity  
        self.size = 0  
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
      
        str_key = str(key)  

        hash_value = 5381  

        for char in str_key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)

        return hash_value

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        hashed_key = self._hash_mod(key) 
        if self.storage[hashed_key] is not None:  
            new_pair = LinkedPair(key, value)
            new_pair.next = self.storage[hashed_key]
            self.storage[hashed_key] = new_pair
        else: 
            self.storage[hashed_key] = LinkedPair(
                key, value)  
            self.size += 1   

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        hashed_key = self._hash_mod(key)  

        if self.storage[hashed_key] is None:  
            print("Warning: key not found")
        else:
            node = self.storage[hashed_key]
            prev_node = None
            while node:  
                if node.key != key: 
                    prev_node = node  
                    node = node.next
                else:  
                    if node.next is None: 
                        if prev_node is None:  
                            
                            self.storage[hashed_key] = None
                            self.size -= 1 
                            return
                        else:  
                            prev_node.next = None
                            self.size -= 1 
                            return
                    else:  
                        if prev_node is None: 
                            self.storage[hashed_key] = node.next
                            self.size -= 1
                            return
                        else:  
                            prev_node.next = node.next  
                            self.size -= 1
                            return
            return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Return None if the key is not found.
        Fill this in.
        '''
        hashed_key = self._hash_mod(key) 
        node = self.storage[hashed_key]  
        while node is not None:  
            if node.key != key:  
                node = node.next   
            else:  
                return node.value  
        return None 

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.capacity *= 2  
        old_storage = self.storage
        
        self.storage = [None] * self.capacity

        for each_bucket in old_storage:  
            curr_bucket = each_bucket  
            while curr_bucket:  
                self.insert(curr_bucket.key, curr_bucket.value)
                curr_bucket = curr_bucket.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")