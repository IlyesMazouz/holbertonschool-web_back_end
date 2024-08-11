#!/usr/bin/env python3
"""
This module defines a Cache class for storing and retrieving data in Redis
It includes decorators to count function calls and store call history
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


def call_history(method: Callable) -> Callable:

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache:

    def __init__(self):

        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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


def replay(method: Callable):

    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for input_data, output_data in zip(inputs, outputs):
        print(
            f"{method.__qualname__}(*{input_data.decode('utf-8')}) -> {output_data.decode('utf-8')}"
        )
