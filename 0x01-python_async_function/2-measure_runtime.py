#!/usr/bin/env python3
"""import wait_n from 1-concurrent_coroutine into 2-measure_runtime.py.

measure_time function whick takes integers n and max_delay as
arguments for measuring total execution time for wait_n(n, max_delay),
and returns total_time / n. Function returns a float.

Time module is used to measure an approximate elapsed time.
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function returns total execution time for wait_n"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time/n)
