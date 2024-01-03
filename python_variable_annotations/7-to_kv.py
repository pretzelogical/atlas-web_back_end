#!/usr/bin/env python3
from typing import Tuple
""" type-annotated function to_kv"""


def to_kv(k: str, v: float) -> Tuple[str, float]:
    """
    returns a tuple of a string and a float
    : k(str) : key
    : v(float) : value
    : return(Tuple[str, float]) : tuple of key and value squared
    """
    return (k, v**2)
