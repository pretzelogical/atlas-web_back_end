#!/usr/bin/env python3
""" Server class that paginates a database """
import csv
from typing import List, Tuple
import math


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            Gets a dictionary that would be returned as a json object for
            a hypermedia link
            : page(int) : page number (1-indexed)
            : page_size(int) : page size
            : return(dict) : dictionary that would be returned as a json object
            for a hypermedia link

            return fields:
            {
                page_size: length of the returned dataset,
                page: current page number,
                data: the dataset page,
                next_page: number of the next page or None if no page,
                prev_page: number of the previous page or None if no page,
                total_pages: the total number of pages in the
                             dataset as an integer
            }
        """
        data = self.get_page(page, page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": (page + 1 if (page + 1) * page_size
                          < len(self.dataset()) else None),
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }
