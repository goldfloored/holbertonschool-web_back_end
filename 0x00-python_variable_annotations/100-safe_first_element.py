#!/usr/bin/env python3

"""get first element in List."""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return first element of the arguments if it is a list otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
