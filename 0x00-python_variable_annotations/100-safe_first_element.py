#!/usr/bin/python3
"""
Module for safe_first_element function
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence or None if empty
    
    Parameters:
    lst (Sequence[Any]): An iterable sequence of elements
    
    Returns:
    Union[Any, None]: The first element of the sequence or None if empty
    """
    if lst:
        return lst[0]
    else:
        return None
