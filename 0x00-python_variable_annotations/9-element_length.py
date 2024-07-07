#!/usr/bin/python3
"""
Module for element_length function
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths
    
    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences
    
    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]
