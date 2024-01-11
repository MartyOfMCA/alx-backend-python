#!/usr/bin/env python3
"""
Define a type-annotated function that accepts
a float and returns a function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiples a float
    by the given multiplier.

    Parameters:
        multiplier : float
        The value to multiply by.

    Returns:
        A function that takes a float
        and returns the product of the float.
    """
    def make_nest_multiplier(mul: float) -> float:
        """
        Computer the product of two floating
        point values in both inner and
        outer functions.

        Parameters
            mul : float
            The value to multiply by.

        Returns:
            The product of `mul` and
            `multiplier`
        """
        return (mul * multiplier)

    return (make_nest_multiplier)
