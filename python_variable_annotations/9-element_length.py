#!/usr/bin/env python3
""" Function element_length with duck typed type checking """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Makes a list of tuples with the element and its length.
    : lst(Iterable[Sequence]) : The list to iterate.
    : return(List[Tuple[Sequence, int]]) :
        A list of tuples with the element and its length.
     """
    return [(i, len(i)) for i in lst]
