#!/usr/bin/env python3
""" FIFO cache system that inherits from BaseCaching """
from queue import Queue
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Cache system that works on the First in First out principle """
    def __init__(self):
        super().__init__()
        self.queue = Queue()

    def put(self, key, item):
        """
            Add an item to the cache and remove if
            len(self.cache_date) > BaseCaching.MAX_ITEMS
        """
        if key is None or item is None:
            return
        self.queue.put(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.queue.get())

    def get(self, key):
        """ Get an item by it's key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
