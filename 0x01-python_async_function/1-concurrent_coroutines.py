#!/usr/bin/env python3
""" waits for random delay """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for ran delay until max_delay """
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delays = await asyncio.gather(*tasks)

    return delays