#!/usr/bin/env python3
"""get key and value frpm dictionnary"""

from typing import Tuple, Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    '''
    return key and value of the dict if it exists
    '''
    if key in dct:
        return dct[key]
    else:
        return default
