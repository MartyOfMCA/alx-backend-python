#!/usr/bin/env python3
"""
Define an asynnchronous coroutine that accepts
a number, waits for a random time then return
the given number.
"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and
    `max_delay` before returning the
    actual delay time.

    Parameters:
        max_delay : int, optional
        The maximum wait time for the
        function.

    Returns:
        The actual wait time.
    """
    delay: float = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
