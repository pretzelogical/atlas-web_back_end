#!/usr/bin/env python3
""" Server class that paginates a database """
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Gets the start and end index of a list
        : page(int) : page number (1-indexed)
        : page_size(int) : page size
        : return(tuple[int, int]) : start and end index of a list
    """
    return ((page - 1) * page_size, page * page_size)


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
        """
            Gets a page of data from the database
            : page(int) : page number (1-indexed)
            : page_size(int) : page size
            : return(list[list]) : page of data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        i_range = index_range(page, page_size)
        return self.dataset()[i_range[0]:i_range[1]]
