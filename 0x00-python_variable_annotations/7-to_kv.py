#!/usr/bin/env python3
"""
Define a type-annotated function that accepts
a string and an int or floating point value
to generate a tuple.
"""
from typing import (
        Tuple,
        Union
        )


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing a string and
    the square of the given number.

    Parameters
    v : string
        The first value for the tuple.
    v : int | float
        The second number for the tuple.
        Could be of type int or float.

    Return
        A tuple containing the string passed
        as an argument and the square of the
        second argument.
    """
    return (k, v * v,)
