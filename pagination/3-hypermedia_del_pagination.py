#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """
    server class to paginate a database of popular baby names
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        retrieve hypermedia information for a given index
        """
        assert index is None or (
            isinstance(index, int) and 0 <= index < len(self.indexed_dataset())
        ), "Index is out of range."
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be a positive integer."

        if index is None:
            index = 0

        current_data = []
        next_index = None

        while len(current_data) < page_size and index < len(self.indexed_dataset()):
            try:
                current_data.append(self.indexed_dataset()[index])
            except KeyError:
                break
            index += 1

        if index < len(self.indexed_dataset()):
            next_index = index

        hypermedia_info = {
            "index": index - len(current_data),
            "data": current_data,
            "page_size": page_size,
            "next_index": next_index,
        }

        return hypermedia_info
