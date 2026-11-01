#!/usr/bin/env python3

"""
contains an async function that calls another async function
"""

import asyncio
import time
import random
import importlib
from typing import List

# imports a function with a file that has a hyphen
my_module = importlib.import_module("0-basic_async_syntax")


async def wait_n(n: int, max_delay: int = 10) -> List[float]:

    """
    calls wait_random n times and returns the fastest wait time first
    """

    tasks = []
    results = []

    for _ in range(n):
        tasks.append(my_module.wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
