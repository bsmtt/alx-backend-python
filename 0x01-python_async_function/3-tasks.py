#!/usr/bin/env python3
""" returns random delay """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ Waits for random delay """
    return asyncio.create_task(wait_random(max_delay))