#!/usr/bin/env python3i
"""
This module contains an async
routine that spawns multiple
wait_random coroutines and
returns the delays in ascending
order without using sort().
"""

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times
    with the specified max_delay.

    Args:
        n (int): Number of times
        to spawn wait_random.
        max_delay (int): Maximum
        delay for wait_random.

    Returns:
        List[float]: List of all
        the delays in ascending
        order.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    # Break the line into two parts for clarity
    coroutines = (wait_random(max_delay) for _ in range(n))
    delay_list = await asyncio.gather(*coroutines)
    return sorted(delay_list)
