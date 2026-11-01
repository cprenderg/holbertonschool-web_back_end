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

    wait_times = []

    for _ in range(n):
        new_time = await my_module.wait_random(max_delay)
        wait_times.append(new_time)

    return wait_times
