#!/usr/bin/env python3
""" An asynchronous generator """
import asyncio
import random


async def async_generator() -> float:
    """
    Loops 10 times, each time waiting one second and the yielding
    a random number between 0 and 10
    : return(float) : a random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
