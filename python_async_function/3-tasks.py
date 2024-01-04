#!/usr/bin/env python3
""" Creating an asyncio task from an async function """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task from an async function
    : max_delay(int) : max amount to randomly wait
    : return(asyncio.Task) : asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))
