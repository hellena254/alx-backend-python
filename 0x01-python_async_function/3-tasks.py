#!/usr/bin/env python3
import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
    - max_delay (int): The maximum delay time in seconds for wait_random.

    Returns:
    - asyncio.Task: The asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
