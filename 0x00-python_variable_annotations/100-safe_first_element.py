#!/usr/bin/env python3
"""
Define a duck-type annotated function that
safely returns the first element in a list.
"""
from typing import (
        Sequence,
        Any,
        Union
        )


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely fetch the first element from a
    supposed list.

    Parameters:
        lst : any
        Any value supposed to be a list.

    Returns:
        The first element so long as
        `lst` is a list otherwise
        None
    """
    if lst:
        return lst[0]
    else:
        return None
