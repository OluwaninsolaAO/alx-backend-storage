#!/usr/bin/env python3
"""0. Writing strings to Redis"""
from typing import Union
from redis import Redis
from uuid import uuid4


class Cache:
    """A Cache class using Redis as storage"""

    def __init__(self) -> None:
        """Initializes a new Cache instance"""
        self._redis = Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis using a random key
        and return the key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
