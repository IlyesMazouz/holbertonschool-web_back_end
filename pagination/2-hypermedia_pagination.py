#!/usr/bin/env python3
"""
a get_hyper method that takes the same arguments (and defaults)
as get_page and returns a dictionary containing the following key-value pairs
"""
import csv
from typing import List
import math


class Server:
    """
    server class to paginate a database of popular baby names
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        retrieve a page of data from the dataset
        """
        assert isinstance(page, int) and page > 0, "must be a positive integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be a positive integer."

        start_index, end_index = self.index_range(page, page_size)

        if start_index >= len(self.dataset()):
            return []

        return self.dataset()[start_index:end_index]

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        calculate the start and end index of a page for pagination
        """
        total_items = len(self.dataset())
        start_index = (page - 1) * page_size
        end_index = min(start_index + page_size, total_items)
        return start_index, end_index

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        retrieve hypermedia information for a page
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hypermedia_info = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }

        return hypermedia_info
