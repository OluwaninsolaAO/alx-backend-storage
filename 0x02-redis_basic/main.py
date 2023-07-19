#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

TEST_CASES_2 = ['July', '19th', 2023]

for value in TEST_CASES_2:
    key = cache.store(value)
    print(f'[{key}] str: {cache.get_int(key)} int: {cache.get_str(key)}')
