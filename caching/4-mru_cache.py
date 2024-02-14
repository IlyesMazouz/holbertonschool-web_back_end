#!/usr/bin/env python3
"""MRU caching module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                most_recent_key = self.usage_order.pop()
                del self.cache_data[most_recent_key]
                print("DISCARD:", most_recent_key)
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
