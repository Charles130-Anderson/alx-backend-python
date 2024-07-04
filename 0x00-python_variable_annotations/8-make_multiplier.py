#!/usr/bin/env python3


'''A module that returns a function'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by a float'''
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
