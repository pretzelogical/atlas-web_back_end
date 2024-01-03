#!/usr/bin/env python3
from typing import List, Union
""" type-annotated function sum_mixed_list """


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns the sum of a list of integers and floats
    : mxd_list(List[Union[int, float]]) : mixed list of ints and floats
    : return(float) : sum of the list of ints and floats
    """
    return sum(mxd_lst)
