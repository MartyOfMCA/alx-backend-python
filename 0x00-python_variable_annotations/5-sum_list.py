#!/usr/bin/env python3
"""
Define a type-annotated function that accepts
a list of float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of the list of floating
    point values.

    Parameters
    input_list : list
        The list of floating point numbers.

    Return
        The sum of the floating point values
        as a float.
    """
    return (sum(input_list))
