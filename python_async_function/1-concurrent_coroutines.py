#!/usr/bin/env python3
""" Async routine created from previous task. """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns n random delays between 0 and max_delay
    in ascending order.
    : n(int) : Number of delays to generate.
    : max_delay(int) : Maximum delay value.
    : return(list) : List of delays.
    """
    tasks: List[asyncio.Task] = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)
    return delays