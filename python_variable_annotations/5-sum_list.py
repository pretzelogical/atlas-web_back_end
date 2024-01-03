#!/usr/bin/env python3
from typing import List
""" Type-annotated function sum_list """


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of all elements in a list
    : input_list(List[float]) : list of floats
    : return(float) : sum of all elements in the list
    """
    return sum(input_list)
