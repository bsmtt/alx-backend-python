#!/usr/bin/env python3
""" waits for random delay """

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for ran delay until max_delay """
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    delays = await asyncio.gather(*tasks)

    return delays