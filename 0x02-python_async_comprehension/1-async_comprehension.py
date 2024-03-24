#!/usr/bin/env python3
"""Import async_generator from 0-async_generator and  write a coroutine
called async_comprehension which takes no arguments.

The coroutine collects 10 random numbers using an async comprehensing
over async_generator, and returns the 10 random numbers.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Function returns the 10 random numbers"""
    results = [i async for i in async_generator()]
    return results
