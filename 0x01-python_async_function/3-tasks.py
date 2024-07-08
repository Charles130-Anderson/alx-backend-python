#!/usr/bin/env python3
"""
Creates an asyncio Task for wait_random.
"""

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a task for the scheduler.

    Args:
        max_delay (int): Maximum delay
        for wait_random.

    Returns:
        asyncio.Task: Task object.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
