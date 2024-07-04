#!/usr/bin/env python3

"""
Zooms in on a tuple by repeating each element based on a given factor.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in a tuple by repeating each element based on a given factor.

    Args:
        lst (Tuple): The tuple of elements to zoom in on.
        factor (int, optional): The zoom factor (default is 2).

    Returns:
        List:Zoomed-in list with each element repeated `factor` times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
