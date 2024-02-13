#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basicCache inherits from BaseCaching and
     is a caching system without limit"""

    def put(self, key, item):
        """add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key is not None:
            return self.cache_data.get(key)
        return None
