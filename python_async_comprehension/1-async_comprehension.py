#!/usr/bin/env python3
""" Consuming values from a async comprehension """
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    Returns a list of 10 numbers using an async comprehension.
    : return(list[float]) : list of 10 random floats
    """
    return [i async for i in async_generator()]
