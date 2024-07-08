#!/usr/bin/env python3
"""
This module contains an async
routine that spawns multiple
wait_random coroutines and returns
their delays in ascending order.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with
    the specified max_delay and
    return the list of delays in
    ascending order.

    Args:
        n (int): The number of
        times to spawn wait_random.
        max_delay (int): The
        maximum delay in seconds.

    Returns:
        List[float]: The list of
        delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
