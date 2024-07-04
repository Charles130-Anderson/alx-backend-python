#!/usr/bin/env python3

"""
Zooms in on a list by repeating each element based on a given factor.
"""

from typing import Union, Any, Mapping, Tuple, List


def zoom_array(lst: List, factor: int = 2) -> List:
    """
    Zooms in on a list by repeating each element based on a given factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
