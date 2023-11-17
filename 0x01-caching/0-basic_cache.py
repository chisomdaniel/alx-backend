#!/usr/bin/env python3
'''Basic dictionary'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A caching system'''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''puts data into the cache'''
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''get data from the cache'''
        if key is None:
            return None
        return self.cache_data.get(key, None)

