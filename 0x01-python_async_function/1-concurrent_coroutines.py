#!/usr/bin/env python3
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.

    Args:
    - n (int): The number of times to spawn wait_random.
    - max_delay (int): The maximum delay time in seconds for wait_random.

    Returns:
    - List[float]: A list of all the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
