#!/usr/bin/env python3
"""Main 100"""
import time
import redis

get_page = __import__('web').get_page
url = 'http://slowwly.robertomurray.co.uk'

for i in range(20):
    s = time.perf_counter()
    get_page(url)
    print(f'({i}) loads @ {time.perf_counter() - s} seconds')
    time.sleep(1)


cache = redis.Redis()
print(cache.get('count:' + url))
