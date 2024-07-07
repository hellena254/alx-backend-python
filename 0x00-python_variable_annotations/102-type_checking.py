#!/usr/bin/python3
"""
Module for zoom_array function
"""

from typing import Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in on an array by repeating each item a specified number of times
    
    Parameters:
    lst (Tuple[int, ...]): The tuple of integers to zoom in on
    factor (int, optional): The zoom factor (default is 2)
    
    Returns:
    Tuple[int, ...]: The zoomed-in tuple
    """
    zoomed_in = tuple(item for item in lst for i in range(factor))
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
