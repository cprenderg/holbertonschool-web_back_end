#!/usr/bin/env python3

"""
calculates the run time of wait_n
"""

import importlib
import time
import asyncio

# imports a function with a file that has a hyphen
my_module = importlib.import_module("1-concurrent_coroutines")


def measure_time(n: int, max_delay: int) -> float:

    """
    calculates the average run time for each wait_random
    """

    start = time.perf_counter()

    run_times = asyncio.run(my_module.wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    average_time = total_time / n

    return average_time
