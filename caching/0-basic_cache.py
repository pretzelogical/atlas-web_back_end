#!/usr/bin/env python3
""" Caching system that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching system that allows for putting and getting data """

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by it's key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
