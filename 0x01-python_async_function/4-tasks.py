#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return sorted list of max delay of execution"""
    x = await asyncio.gather(*(task_wait_random(max_delay) for i in range(n)))
    return sorted(x)
