#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel"""
    a = time.perf_counter()
    b = await asyncio.gather(*(async_comprehension() for i in range(4)))
    c = time.perf_counter() - a
    return c
