#!/usr/bin/env/python3
""" LIFO caching system that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ caching system that works on the Last in First Out principle """

    def __init__(self):
        """ initialize the class """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
            Add an item to the cache and remove if
            len(self.cache_data) > BaseCaching.MAX_ITEMS
        """
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.pop()
                self.queue.append(key)
                return
            remove_key = self.queue.pop()
            print(f"DISCARD: {remove_key}")
            self.cache_data.pop(remove_key)
            self.cache_data[key] = item
            self.queue.append(key)
            return
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Get an item by it's key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
