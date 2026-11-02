#!/usr/bin/env python3

"""
returns a number between 0 and 10
"""

import asyncio
import random
import time
from typing import List


async def async_generator() -> float:
    """
    generates 10 different floats
    """

    for _ in range(0, 10):
        random_number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_number
