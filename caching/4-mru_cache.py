#!/usr/bin/env python3
""" Cache that uses MRU to decide which item to evict """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Cache that removes the most recently used item """
    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.queue = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.update({key: item})
                self.queue.move_to_end(key)
                return
            last_key, _ = self.queue.popitem()
            print(f"DISCARD: {last_key}")
        self.queue[key] = item
        self.cache_data = dict(self.queue)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.queue.move_to_end(key)
        return self.cache_data[key]
