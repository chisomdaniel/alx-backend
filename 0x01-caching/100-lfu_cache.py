#!/usr/bin/env python3
'''LFU caching'''
from base_caching import BaseCaching


def lowest_idx(track_dict):
    '''return the key that has the lowest
    index in a dictionary'''
    idx = list(track_dict.keys())[0]
    lowest = track_dict[idx]
    for i, j in track_dict.items():
        if lowest > j:
            lowest = j
            idx = i
    return idx


class LFUCache(BaseCaching):
    '''the LFU cache'''

    def __init__(self):
        super().__init__()
        self.track = {}
        self._idx = 0

    @property
    def idx(self):
        '''get the idx'''
        self._idx += 1
        return self._idx

    def put(self, key, item):
        '''put data using the LFU policy'''
        if key is None or item is None:
            return

        if key in self.track:
            self.track[key] += 1
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least = lowest_idx(self.track)
            del self.cache_data[least]
            print('DISCARD: {}'.format(least))
            del self.track[least]
        self.cache_data[key] = item
        self.track[key] = 0

    def get(self, key):
        '''get an element from the cache'''
        if key is None:
            return None

        value = self.cache_data.get(key)
        if value is None:
            return None
        self.track[key] += 1
        return self.cache_data.get(key)
