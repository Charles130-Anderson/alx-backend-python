#!/usr/bin/env python3

from typing import List

'''
Convert wait_n to task_wait_n.
Similar to wait_n, uses task_wait_random.
'''


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Run async function n times.'''
    modified_random = __import__('3-tasks').task_wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await modified_random(max_delay))
        i += 1

    return sorted(delay_list)
