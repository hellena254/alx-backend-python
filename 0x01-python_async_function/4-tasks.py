#!/usr/bin/env python3
import asyncio
from typing import List
from 3-tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with the specified max_delay.

    Args:
    - n (int): The number of times to spawn task_wait_random.
    - max_delay (int): The maximum delay time in seconds for task_wait_random.

    Returns:
    - List[float]: A list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    
    # Manually sort the list without using sort()
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
