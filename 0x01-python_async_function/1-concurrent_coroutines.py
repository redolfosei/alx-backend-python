#!/usr/bin/env python3
"""Async routine functiom 'wait_n' which takes in 2 int arguments
(in this order): n and max_delay. Spawn wait_random n times with
the specified max_delay. wait_random is imported from
'0-basic_async_function'

'wait_n' returns the list of all the delays (float values) in
ascending order without using sort() because of concurrency.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function spawns wait_random n times"""
    tasks = []
    delays = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
