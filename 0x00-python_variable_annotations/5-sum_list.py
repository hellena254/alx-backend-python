#!/usr/bin/python3
"""
Module for sum_list function
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats
    
    Parameters:
    input_list (List[float]): The list of float numbers
    
    Returns:
    float: The sum of the float numbers in the list
    """
    return sum(input_list)
