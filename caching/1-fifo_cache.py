#!/usr/bin/env python3
"""FIFO caching module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD:", first_key)
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
