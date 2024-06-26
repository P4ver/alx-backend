#!/usr/bin/python3
"""LIFO Caching,"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """use self.cache_data - dictionary from the parent class
    BaseCaching
    """

    def __init__(self):
        """ init"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data the item value for
        the key key
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)

    def is_full(self):
        """ if the numb of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """ print DISCARD: with the key discarded and following by a
        new line -pop-
        """
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
