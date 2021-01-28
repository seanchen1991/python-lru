from doubly_linked_list import DoublyLinkedList

"""
Our LRUCache class keeps track of the max number of nodes it
can hold, the current number of nodes it is holding, a doubly-
linked list that holds the key-value entries in the correct 
order, as well as a storage dict that provides fast access
to every node stored in the cache.
"""
class LRUCache:
    def __init__(self, capacity=100):
        # the max number of entries the cache can hold
        self.capacity = capacity
        # the hash map for storing entries as key-value pairs
        # it's what allows us to efficiently fetch entries
        self.storage = dict()
        # a doubly linked list for keeping track of the order
        # of elements in our cache
        self.order = DoublyLinkedList()
    
    def insert(self, key, value):
        # if the key is already in the cache, overwrite its value
        if key in self.storage:
            entry = self.storage[key]
            entry.data = (key, value)

            # touch this entry to move it to the head of the
            # linked list 
            self.touch(entry)
            return

        # check if our cache is at max capacity to see if we 
        # need to evict the oldest entry 
        if len(self.storage) == self.capacity:
            self.evict()

        # add the key and value as a node at the head of 
        # our doubly linked list 
        self.order.add_to_head((key, value))

        # add the linked list node as the value of the key
        # in our storage dictionary
        self.storage[key] = self.order.head
    
    def touch(self, entry):
        self.order.move_to_front(entry)
    
    def evict(self):
        # delete the key-value pair from the storage dict 
        # we can get the oldest entry's key by accessing 
        # it from the tail of the linked list 
        key_to_delete = self.order.tail.data[0]
        del self.storage[key_to_delete]

        # remove the tail entry from our linked list 
        self.order.remove_from_tail()
    
    def fetch(self, key):
        if key not in self.storage:
            return
    
        entry = self.storage[key]
        self.touch(entry)
        return entry.data[1]
