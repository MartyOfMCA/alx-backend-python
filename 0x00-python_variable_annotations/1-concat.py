#!/usr/bin/env python3
"""
Define a type-annotated function accepting two
strings and return a concatenation of
both strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate any two given strings.

    Parameters
    str1 : string
        The first string.
    str2 : string
        The second string

    Return
        A concatanation of the two strings.
    """
    return (f"{str1}{str2}")
