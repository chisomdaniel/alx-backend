#!/usr/bin/env python3
'''fifo caching'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''the fifo cache'''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''put data using the FIFO policy'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = list(self.cache_data.keys())[0]
            del self.cache_data[first]
            print('DISCARD: {}'.format(first))

    def get(self, key):
        '''get an element from the cache'''
        if key is None:
            return None

        value = self.cache_data.get(key)
        if value is None:
            return None
        return self.cache_data.get(key)
