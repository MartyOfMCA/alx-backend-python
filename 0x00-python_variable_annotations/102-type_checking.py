#!/usr/bin/env python3
"""
Defines a type-annotated function that returns
a list of numbers multiplied by the given
factor.
"""


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Returns a list of numbers multiplied by the
    given factor.

    Parameters:
        lst : tuple
        A tuple of numbers.

        factor: int, default of 2
        The zoom factor

    Returns:
        A list of numbers resulting from
        multiplying the tuple elements
        against the factor.
    """
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]

    return (zoomed_in)
