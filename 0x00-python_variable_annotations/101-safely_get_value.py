#!/usr/bin/env python3
"""
Define a type-annotated function to safely
get the values of a dictionary.
"""
from typing import (
        Union,
        Any,
        Mapping,
        TypeVar
        )
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely fetch the value macthing the given
    key in the dictionary.

    Paramaters:
        dct : dict
        A dictionary of key-value pairs.

        key : any
        The key to be used to fetch a value
        from the dictionary.

        default : any, optional
        Set to None

    Returns:
        The value matching the given key
        otherwise None.
    """
    if key in dct:
        return dct[key]
    else:
        return default
