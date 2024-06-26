#!/usr/bin/python3
""" Basic dictionary."""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching."""

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data the item value for
        the key key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data linked to key. If key is
        None or if the key doesn’t exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
