#!/usr/bin/env python3
"""
Define a function that executes an async
coroutine multiple times in parallel.
"""
import asyncio
from time import perf_counter


async def measure_runtime() -> float:
    """
    Measures the execution time taken to
    run a coroutine multiple times in
    parallel. Asynchronous coroutines run
    in parallel would have same execution
    time but synchronous coroutine execution
    would produce an execution time of the
    product of number of executions by
    total number of calls.

    Returns:
        The total execution time taken to
        execute all coroutines. Each
        coroutine takes up to 10 seconds.
    """
    async_comps = []
    start_time = perf_counter()
    async_comp = __import__("1-async_comprehension")\
        .async_comprehension
    async_comps = [async_comp() for i in range(4)]

    await asyncio.gather(*async_comps)
    end_time = perf_counter()

    return (end_time - start_time)
