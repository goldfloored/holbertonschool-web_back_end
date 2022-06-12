#!/usr/bin/env python3
"""callable annotation module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function to return a function that multiplay a float"""
    def multiplyy(y: float):
        """function to multiply a float"""
        return y * multiplier
    return multiplyy
