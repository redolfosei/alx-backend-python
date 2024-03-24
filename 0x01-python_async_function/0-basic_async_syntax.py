#!/usr/bin/env python3
"""Asynchronous coroutine which takes in an integer argument
(max_delay, with a default value of 10) with a random delay time
between 0 and max_delay.

Use of the random module is allowed.
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Function waits on a random time"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
