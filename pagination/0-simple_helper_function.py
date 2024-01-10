#!/usr/bin/env python3
""" Function index_range that gets the start and end index of a list """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Gets the start and end index of a list
        : page(int) : page number (1-indexed)
        : page_size(int) : page size
        : return(tuple[int, int]) : start and end index of a list
    """
    return ((page - 1) * page_size, page * page_size)
