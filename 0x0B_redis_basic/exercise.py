#!/usr/bin/env python3
"""
this module defines a Cache class for storing and retrieving data in Redis
It also includes a decorator to count the number of times a method is called
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:

    @wraps(method)
    def wrapper(self, *args, **kwargs):

        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:

    def __init__(self):

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str,
        fn: Optional[Callable[[bytes], Union[str, int, bytes]]] = None
    ) -> Union[str, int, bytes, None]:

        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:

        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:

        return self.get(key, lambda d: int(d))
