#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict, Tuple, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Gets the start and end index of a list
        : page(int) : page number (1-indexed)
        : page_size(int) : page size
        : return(tuple[int, int]) : start and end index of a list
    """
    return ((page - 1) * page_size, page * page_size)


class UltraList(list):
    """
        Acts just like a normal list except it returns the index
        along with the item in a tuple
    """
    def __getitem__(self, index: int) -> Tuple[int, Any]:
        """
            Gets the index along with the item in a tuple
            : index(int) : index to get
            : return(tuple[int, Any]) : index and item in a tuple if getting
                                        one or an array of tuples if many
        """
        if isinstance(index, int):
            return (index, super().__getitem__(index))
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            getitem = super().__getitem__
            return [(i, getitem(i))
                    for i in range(start, stop, step)]


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = UltraList(dataset)
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            Gets a dictionary that would be returned in a hypermedia link
            : index(int) : index to get
            : page_size(int) : page size
            : return(dict) : dictionary
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        assert index < len(self.indexed_dataset()) / page_size

        end = index + page_size
        # print(data_range)
        data = self.indexed_dataset()[index:end]
        data_stripped = [item[1] for item in data]

        return {
            "index": data[0][0],
            "data": data_stripped,
            "page_size": page_size,
            "next_index": data[-1][0] + 1,
        }
