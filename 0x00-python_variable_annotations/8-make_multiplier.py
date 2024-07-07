#!/usr/bin/python3
"""
Module for make_multiplier function
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier
    
    Parameters:
    multiplier (float): The multiplier
    
    Returns:
    Callable[[float], float]: A function that takes a float and returns its product with the multiplier
    """
    def multiplier_func(num: float) -> float:
        return num * multiplier
    
    return multiplier_func
