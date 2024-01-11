#!/usr/bin/env python3
"""
Define a type-annotated function which accepts
a list of integers and floats returning the
sum as a float.
"""
from typing import (
    List,
    Union
    )


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    """
    Computer the sum of items in the given
    list.

    Parameters
    mixed_list : list
        A list of integers and floats.

    Return
        The sum of items in the list as
        a floating point number.
    """
    return (sum(mixed_list))
