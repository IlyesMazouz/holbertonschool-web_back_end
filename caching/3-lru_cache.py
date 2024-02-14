#!/usr/bin/env python3
"""LRU caching module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_queue = []

    def put(self, key, item):
        """add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.cache_queue.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            if key in self.cache_queue:
                self.cache_queue.remove(key)
            self.cache_queue.append(key)

    def get(self, key):
        """get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_queue:
            self.cache_queue.remove(key)
        self.cache_queue.append(key)
        return self.cache_data[key]
