#!/usr/bin/env python3
"""0. Writing strings to Redis"""
from typing import Union, Optional, Callable
import redis
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """that takes a single method Callable argument and
    returns a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Inner Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for
    a particular function"""
    in_key = method.__qualname__ + ':inputs'
    out_key = method.__qualname__ + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Inner Wrapper function"""
        self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(out_key, str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    """displays the history of calls of a particular function"""
    cache = redis.Redis()
    name = method.__qualname__
    input_key = name + ':inputs'
    ouput_key = name + ':outputs'
    assert cache.llen(input_key) == cache.llen(ouput_key)
    inputs = cache.lrange(input_key, 0, cache.llen(input_key))
    outputs = cache.lrange(ouput_key, 0, cache.llen(ouput_key))

    print("{} was called {} times:".format(name, cache.llen(input_key)))

    for input, output in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(name,
                                     input.decode('utf-8'),
                                     output.decode('utf-8')))


class Cache:
    """A Cache class using Redis as storage"""

    def __init__(self) -> None:
        """Initializes a new Cache instance"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis using a random key
        and return the key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """Takes a key string argument and an optional Callable
        argument named fn to convert the data back to the
        desired format."""
        data = self._redis.get(key)

        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Takes a key string argument and Converts data
        from bytes to string"""
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Takes a key string argument and Converts data
        from bytes to integer"""
        data = self._redis.get(key)
        try:
            data = int(data)
        except ValueError:
            data = 0
        return data
