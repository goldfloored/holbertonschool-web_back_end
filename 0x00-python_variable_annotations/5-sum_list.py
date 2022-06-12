#!/usr/bin/env python3
"""module to return the sum of list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return the sum of floats in the list"""
    sum = 0.0
    for val in input_list:
        sum += val
    return sum
