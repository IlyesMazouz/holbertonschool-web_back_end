#!/usr/bin/env python3
"""LIFO caching module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_queue = []

    def put(self, key, item):
        """add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.cache_queue.pop(-1)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.cache_queue.append(key)

    def get(self, key):
        """get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
