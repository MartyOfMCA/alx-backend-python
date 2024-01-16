#!/usr/bin/env python3
"""
Define a coroutine yielding a random number
after waiting for a second. Coroutine
repeats for 10 times.
"""
from typing import Generator
from random import uniform
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    Yields a random number between 0 and
    10 for 10 times. Coroutine runs
    10 times asynchronously.

    Returns:
        An asynchronous generator of floating
        point values indicating the random
        numbers yielded.
    """
    for increment in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
