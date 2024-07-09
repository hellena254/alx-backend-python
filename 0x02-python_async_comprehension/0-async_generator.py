#!/usr/bin/env python3
"""
Async Generator
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generates 10 random numbers between 0 and 10.
    Each number is generated after a 1-second delay.
    """
    for i in range(10):
        await asyncio.sleep(1)
	yield random.random() * 10
