#!/usr/bin/python3
"""
FIFO Caching Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching class
    """

    def get(self, key):
        """ get the value of the key """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]

    def put(self, key, item):
        """ put the value to key """
        if key is None or item is None:
            return
        if len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
        elif key in self.cache_data.keys():
            self.cache_data[key] = item
        else:
            print("DISCARD: {}".format(next(iter(self.cache_data))))
            self.cache_data.pop(next(iter(self.cache_data)))
            self.cache_data[key] = item
