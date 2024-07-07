#!/usr/bin/python3
"""
Module for sum_mixed_list function
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats
    
    Parameters:
    mxd_lst (List[Union[int, float]]): The list of integers and float numbers
    
    Returns:
    float: The sum of the numbers in the list
    """
    return sum(mxd_lst)
