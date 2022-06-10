#!/usr/bin/python3
"""
Caching Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """basic dictionnary caching class"""

    def put(self, key, item):
        """ assign item to keys in dictionnary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get value of the key """
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
