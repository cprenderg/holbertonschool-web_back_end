#!/usr/bin/env python3

"""
creates coroutines to collect numbers from generator
"""

import asyncio
from typing import List

generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    returns a list of numbers from a generator
    """

    numbers = []

    async for number in generator():
        numbers.append(number)

    return numbers
