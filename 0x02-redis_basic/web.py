#!/usr/bin/env python3
"""5. Implementing an expiring web cache and tracker"""

from requests import get
import redis
from functools import wraps
from typing import Callable


def track_page_count(method: Callable) -> Callable:
    """Tracks how many times a particular
    URL was accessed"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        """Inner Wrapper Function"""
        cache = redis.Redis()
        url = args[0]
        key = 'count:' + url
        cache.incr(key)
        page = cache.get(url)
        if page is not None:
            return page.decode('utf-8')
        page = method(*args, **kwargs)
        cache.setex(key, 10, page)
        return page
    return wrapper


def get_page(url: str) -> str:
    """Obtain the HTML content of a particular
    URL and returns it."""
    return get(url).text
