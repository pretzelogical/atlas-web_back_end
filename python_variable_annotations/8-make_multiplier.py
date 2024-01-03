#!/usr/bin/env python3
""" type-annotated function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function make_multiplier
    : multitplier(float) : multiplier to be used
    : return(Callable[[float],[float]]) :
        a function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
