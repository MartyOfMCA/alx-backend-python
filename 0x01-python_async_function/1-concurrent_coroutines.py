#!/usr/bin/env python3
"""
Define an async routine that will spawn
another async coroutine for some given
number of times.
"""
from typing import (
        List,
        Callable,
        Awaitable
        )
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Call an async coroutine that waits for `n`
    number of times.

    Parameters:
        n : int
        The number of times to fire the async
        coroutine.

        max_delay : int
        The maximum wait time for the async
        coroutine.

    Returns:
        A list of floats containing the wait
        times for the async coroutine.
    """
    wait_random: Callable[[float], Awaitable[float]] =\
        __import__("0-basic_async_syntax").wait_random
    my_list: List[float] = []

    for increment in range(0, n):
        my_list.append(await wait_random(max_delay))

    return (sorted(my_list))
