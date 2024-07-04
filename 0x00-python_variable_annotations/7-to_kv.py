#!/usr/bin/env python3


'''a module that takes two arguments and returns a tuple'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''A function that retuns a tuple'''
    return (k, float(v ** 2))
