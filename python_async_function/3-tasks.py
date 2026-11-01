#!/usr/bin/env python3

"""
fetches an asyncio.Task
"""

import importlib
import asyncio

# imports a function with a file that has a hyphen
my_module = importlib.import_module("0-basic_async_syntax")


def task_wait_random(max_delay: int):

    """
    returns a wait_random with type asyncio.Task
    """

    return asyncio.create_task(my_module.wait_random(max_delay))
