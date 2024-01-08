#!/usr/bin/env python3
""" Cache that uses LRU to decide which item to evict. """
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Cache system that uses LRU to decide which item to evict. """

    def __init__(self):
        """ Initialize LRUCache. """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Add an item to the cache and remove if
            len(self.cache_data) > BaseCaching.MAX_ITEMS
        """
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.moveToFrontOfQueue(key)
                return
            remove_key = self.queue.popleft()
            print(f"DISCARD: {remove_key}")
            self.cache_data.pop(remove_key)
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by it's key """
        if key is None or key not in self.cache_data:
            return None
        self.moveToFrontOfQueue(key)
        return self.cache_data[key]

    def moveToFrontOfQueue(self, key):
        """ Moves an item to the front of the
            queue unless it's already there
        """
        if self.queue[0] == key:
            return
        self.queue.remove(key)
        self.queue.append(key)
