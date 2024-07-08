#!/usr/bin/env python3
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
    - max_delay (int): The maximum delay time in seconds for wait_random.

    Returns:
    - asyncio.Task: The asyncio.Task object.
    """
    task = create_task(wait_random(max_delay))
    return task
