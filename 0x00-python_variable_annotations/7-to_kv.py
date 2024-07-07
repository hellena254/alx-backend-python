#!/usr/bin/env python3
"""
Module for to_kv function
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of an int/float
    
    Parameters:
    k (str): The string
    v (Union[int, float]): The number to be squared
    
    Returns:
    Tuple[str, float]: A tuple containing the string and the square of the number
    """
    return (k, float(v ** 2))
