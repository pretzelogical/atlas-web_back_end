#!/usr/bin/env python3
"""
    Using the time module to measure the
    execution time of a program
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Measure the execution time of wait_n n times
        : n(int) : number of times to call wait_n
        : max_delay(int) : maximum delay in seconds
        : return(float) : total time / n
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    return (end - start) / n
