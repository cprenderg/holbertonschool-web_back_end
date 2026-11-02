#!/usr/bin/env python3

"""
calls multiple task_wait_random and returns the wait time in ASC
"""

import asyncio
from typing import List

task_wait = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:

    """
    calls task_wait_random n times and returns the fastest wait time first
    """

    tasks = []
    results = []

    for _ in range(n):
        tasks.append(task_wait(max_delay))

    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
