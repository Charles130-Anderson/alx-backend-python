#!/usr/bin/env python3
"""
Measure average execution time per
iteration of wait_n(n, max_delay).
"""

import asyncio
import time
from typing import List


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total time coroutines took
    to completion.

    Args:
        n (int): Number of iterations.
        max_delay (int): Maximum delay
        for wait_random.

    Returns:
        float: Average execution time per iteration.
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()    
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
