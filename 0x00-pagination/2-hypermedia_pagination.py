#!/usr/bin/env python3
'''Simple pagination'''
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    '''takes two integer arguments page and page_size.
    return a tuple of size two containing a start index and an
    end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters.'''

    start_idx = (page-1) * page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return the valid pages based on the input range'''
        assert ((type(page) == int) and (type(page_size) == int))
        assert ((page > 0) and (page_size > 0))

        idx = index_range(page, page_size)
        if max(idx) > len(self.dataset()):
            return []

        data = [self.__dataset[i] for i in range(idx[0], idx[1])]
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        ''' Hypermedia pagination '''
        data = self.get_page(page, page_size)
        total_page = math.ceil(len(self.__dataset) / page_size)
        new_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': (page+1 if page < total_page else None),
            'prev_page': (page-1 if page != 1 else None),
            'total_pages': total_page
        }

        return new_dict
