#!/usr/bin/env python3
'''lifo caching'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''the lifo cache'''

    def __init__(self):
        super().__init__()
        self.track = []

    def put(self, key, item):
        '''put data using the LIFO policy'''
        if key is None or item is None:
            return

        self.track.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.track[-2]
            del self.cache_data[last]
            print('DISCARD: {}'.format(last))
            self.track.pop(0)

    def get(self, key):
        '''get an element from the cache'''
        if key is None:
            return None

        value = self.cache_data.get(key)
        if value is None:
            return None
        return self.cache_data.get(key)
