#!/usr/bin/python3
""" LIFO Caching Module """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO caching class
    """

    l_key = ""

    def get(self, key):
        """ get the value of the key """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]

    def put(self, key, item):
        """ put item in the dictionary """
        if key is None or item is None:
            return
        if len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            self.l_key = key
        elif key in self.cache_data.keys():
            self.cache_data[key] = item
            self.l_key = key
        else:
            self.cache_data.pop(self.l_key)
            print("Discard {}".format(self.l_key))
            self.cache_data[key] = item
            self.l_key = key
