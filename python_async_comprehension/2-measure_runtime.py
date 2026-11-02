#!/usr/bin/env python3

"""
measures how long four coroutines take to execute
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:

    """
    runs four async_comprehensions simultaneously
    """

    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]

    start = time.perf_counter()
    await asyncio.gather(*tasks)
    end = time.perf_counter()

    return (end - start)
