#!/usr/bin/env python3
"""
Define a type-annotated method to return a
tuple containing a list and it's length
from a list of lists.
"""
from typing import (
        Tuple,
        List,
        Iterable,
        Sequence
        )


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns an object containing an element
    and it's length.

    Parameters:
        lst : list
        A list whose elements are lists

    Returns:
        A tuple containing an element from
        `list_of_list` and its length.
    """
    return [(i, len(i)) for i in lst]
