#!/usr/bin/env python3
""" Task version of wait_n """
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Returns a list of all the delays using a task
    list in ascending order.
    : n(int) : number of delays to create
    : max_delay(int) : maximum delay to create
    : return(list[float]) : list of delays in ascending order.
    """
    tasks: list[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    delays: list[float] = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)
    return delays
