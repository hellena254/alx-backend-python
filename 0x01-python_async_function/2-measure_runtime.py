#!/usr/bin/env python3
from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the average time per task.

    Args:
    - n (int): The number of times to spawn wait_random.
    - max_delay (int): The maximum delay time in seconds for wait_random.

    Returns:
    - float: The average time per task.
    """
    start = time()
    run(wait_n(n, max_delay))
    end = time()
