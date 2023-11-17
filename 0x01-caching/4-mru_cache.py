#!/usr/bin/env python3
'''MRo caching'''
from base_caching import BaseCaching


def highest_idx(track_dict):
    '''return the key that has the highest
    index in a dictionary'''
    idx = list(track_dict.keys())[0]
    highest = track_dict[idx]
    for i, j in track_dict.items():
        if highest < j:
            highest = j
            idx = i
    return idx


class MRUCache(BaseCaching):
    '''the mru cache'''

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
        '''put data using the MRU policy'''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.track[key] = self.idx
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            highest = highest_idx(self.track)
            del self.cache_data[highest]
            print('DISCARD: {}'.format(highest))
            del self.track[highest]
        self.track[key] = self.idx
        self.cache_data[key] = item

    def get(self, key):
        '''get an element from the cache'''
        if key is None:
            return None

        value = self.cache_data.get(key)
        if value is None:
            return None
        self.track[key] = self.idx
        return self.cache_data.get(key)
