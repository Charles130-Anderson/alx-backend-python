#!/usr/bin/env python3

'''
Description: Convert wait_n to task_wait_n.
             Similar to wait_n, uses task_wait_random.
Arguments: n: int, max_delay: int = 10
'''

from typing import List
import asyncio
import random

# Dynamically import task_wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Run task_wait_random and return sorted delay list'''
    spawn_tasks = []
    delay_list = []

    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_tasks.append(delayed_task)

    for task in spawn_tasks:
        await task

    return sorted(delay_list)
