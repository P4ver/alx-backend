#!/usr/bin/python3
""" 1. FIFO caching
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ class FIFOCache inherits from BaseCaching"""

    def __init__(self):
        """ Init"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ assign to the dict self.cache_data the item value for
        the key key.
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key,"""
        return self.cache_data.get(key, None)

    def is_full(self):
        """ If the nmbr in self.cache_data is higher than
        BaseCaching.MAX_ITEMS
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """print DISCARD: with the key discarded and following by
        newline"""
        popped = self.queue.popleft()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
