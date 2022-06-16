#!/usr/bin/env python3
"""pagination module
"""
import csv
import math
from os import preadv
from typing import List
from typing import Tuple
from typing import Dict


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
        """return list"""
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        r = index_range(page, page_size)
        if r[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[r[0]:r[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        page = page
        total_pages = math.ceil(len(dataset) / page_size)
        page_size = len(data)
        prev_page = None
        next_page = None
        if page > 1:
            prev_page = page - 1
        if page < total_pages:
            next_page = page + 1

        d = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return d


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    total_size = page * page_size
    page_n = total_size - page_size
    return (page_n, page)
