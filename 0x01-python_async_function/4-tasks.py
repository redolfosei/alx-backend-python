#!/usr/bin/env python3
"""Function 'wait_n' is altered into a new functiontask_wait_n.
Code is nearly identical to wait_n except task_wait_random is
being called.
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function spawns wait_random n times"""
    tasks = []
    delays = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
