#!/usr/bin/env python3
""" Using asyncio.gather() to run 4 async generators in paralell """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of 4 async generators in paralell
    : return(float) : runtime of 4 async generators in paralell
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return end - start
