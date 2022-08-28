#!/usr/bin/env python3
"""
Redis basic
"""
from functools import wraps
import redis
from typing import Optional, Union, Callable
import uuid


def count_calls(method: Callable) -> Callable:
    """
    Counts the number of calls decorator
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Wrapper
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Stores the history of inputs and outputs for a called function
    """
    inputKey = method.__qualname__ + ":inputs"
    outputKey = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        RPUSH Insert all the specified values at the tail
        of the list stored at key.
        """
        self._redis.rpush(inputKey, str(args))
        output = method(self, *args, *kwds)
        self._redis.rpush(outputKey, str(output))
        return output
    return wrapper


def replay(fn: Callable) -> str:
    """ replay function to display the history of
    calls of a particular function."""
    # method: __qualname__
    method = fn.__qualname__
    inputs = f"{method}:inputs"
    outputs = f"{method}:outputs"
    input_list = fn.__self__._redis.lrange(inputs, 0, -1)
    output_list = fn.__self__._redis.lrange(outputs, 0, -1)
    number = fn.__self__._redis.get(method).decode('utf-8')
    print(f"{method} was called {number} times:")
    for inp, out in zip(input_list, output_list):
        print(f"{method}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


class Cache():
    """Cache class"""

    def __init__(self):
        """Intizializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method should generate a random key
        Return:
            Random generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        for key in self._redis.keys():
            if fn:
                return fn(data)
            return data

    def get_str(self, data: bytes) -> str:
        """method that converts data to string"""
        return data.decode("utf-8")

    def get_int(self, data):
        """method that converts data to int"""
        return int(data)