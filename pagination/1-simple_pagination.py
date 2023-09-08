#!/usr/bin/env python3
"""
pagination script for popular baby names dataset
"""
import csv
from typing import List

class Server:
    """
    server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        cached dataset
        """
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
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

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
