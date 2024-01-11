#!/usr/bin/env python3
"""
Define a type-annotated function to safely
get the values of a dictionary.
"""


def safely_get_value(dct, key, default=None):
    """
    Safely fetch the value macthing the given
    key in the dictionary.

    Paramaters:
        dct : dict
        A dictionary of key-value pairs.

        key : string
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
