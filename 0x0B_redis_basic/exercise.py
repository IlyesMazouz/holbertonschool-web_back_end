#!/usr/bin/env python3
"""
this module defines a Cache class for storing data in Redis
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    cache class that provides a simple interface for storing and retrieving data
    from a Redis database
    """

    def __init__(self):
        """
        initialize the Cache instance with a Redis client and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store data in Redis with a randomly generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
