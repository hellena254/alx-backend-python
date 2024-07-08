#!/usr/bin/env python3
import time
import asyncio
from typing import List
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the average time per task.

    Args:
    - n (int): The number of times to spawn wait_random.
    - max_delay (int): The maximum delay time in seconds for wait_random.

    Returns:
    - float: The average time per task.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
