#!/usr/bin/env python3
"""
Define a function that returns a Task object
representing an async coroutine.
"""
from asyncio import (
        create_task,
        Task
        )


def task_wait_random(max_delay: int) -> Task:
    """
    Return a Task object to an async coroutine.

    Parameters:
        max_delay : int
        THe maximum wait time for the
        async coroutine.

    Returns:
        The asyncio Task to the async
        coroutine.
    """
    return (create_task(__import__("0-basic_async_syntax")
            .wait_random(max_delay)))
