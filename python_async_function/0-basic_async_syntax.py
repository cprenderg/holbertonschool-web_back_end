#!/usr/bin/env python3

"""
contains an async function that waits and returns wait time
"""

import asyncio
import time
import random


async def wait_random(max_delay: int = 10):

    """
    waits and prints a random wait time between - and max_delay
    """

    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
