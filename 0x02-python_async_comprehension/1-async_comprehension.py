#!/usr/bin/env python3

"""Collect numbers via async comprehension."""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect random numbers using comprehension."""
    return [num async for num in async_generator()]
