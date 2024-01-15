#!/usr/bin/env python3
"""
Define an async coroutine that measures
the total execution time for another
async routine.
"""
from asyncio import run
from typing import (
        Callable,
        Awaitable
        )
from time import perf_counter


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time to
    run any async coroutine. Coroutine is
    called `n` number of times with a delay
    of `max_delay`.

    Parameters
        n : the number of times to fire the
        async coroutine.

        max_delay : int
        The maximum wait time for the async
        coroutine.

    Returns:
        The totl execution time taken by
        async coroutine.
    """
    start_time: float = perf_counter()
    run(__import__("1-concurrent_coroutines").wait_n(n, max_delay))
    end_time: float = perf_counter()

    return ((end_time - start_time) / n)
