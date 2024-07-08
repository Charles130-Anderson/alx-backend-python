#!/usr/bin/env python3


from typing import List


''' Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is being
    called.
'''


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Runs an async function for n times and adds the results into a list'''
    modified_random = __import__('3-tasks').task_wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await modified_random(max_delay))
        i += 1

    return sorted(delay_list)
