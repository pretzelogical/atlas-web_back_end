#!/usr/bin/env python3
""" Async routine created from previous task. """
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Returns n random delays between 0 and max_delay
    in ascending order.
    : n(int) : Number of delays to generate.
    : max_delay(int) : Maximum delay value.
    : return(list) : List of delays.
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
