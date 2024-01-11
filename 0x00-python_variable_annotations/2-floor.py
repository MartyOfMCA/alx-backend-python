#!/usr/bin/env python3
"""
Define a type-annotated function to determine
the floor for the given floating point value.
"""
import math


def floor(n: float) -> int:
    """
    Obtain the floor from the given floating
    point number.

    Parameters
    n : float
        The floating point number.

    Return
        The greatest integer less than or
        equals `n`.
    """
    return (math.floor(n))
