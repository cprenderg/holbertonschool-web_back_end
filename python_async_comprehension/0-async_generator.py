#!/usr/bin/env python3

"""
returns a number between 0 and 10
"""

import asyncio
import random
import time
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    generates 10 different floats
    """

    for _ in range(0, 10):
        random_number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_number
