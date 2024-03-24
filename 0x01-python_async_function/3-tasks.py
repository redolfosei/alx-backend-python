#!/usr/bin/env python3
"""Function 'task_wait_random' which takes an integer max_delay
and returns a asyncio.Task. This uses a regular function syntax 
instead of an async syntax

wait_random is imported from 0-basic_async_syntax
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function returns an asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
