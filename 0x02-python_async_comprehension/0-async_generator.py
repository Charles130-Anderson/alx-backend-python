#!/usr/bin/env python3
"""Generate random numbers asynchronously."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield random numbers between zero and ten."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
