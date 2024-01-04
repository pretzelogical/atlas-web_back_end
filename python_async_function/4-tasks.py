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
    tasks = []
    delays = []
    sorted_delays = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    for i in range(n):
        sorted_delays.append(min(delays))
        delays.remove(min(delays))
    return sorted_delays
