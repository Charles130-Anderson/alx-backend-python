#!/usr/bin/env python3
''' Duck typing - first element of a sequence
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Outputs the first element of lst if there is any, otherwise None. '''
    if lst:
        return lst[0]
    else:
        return None
