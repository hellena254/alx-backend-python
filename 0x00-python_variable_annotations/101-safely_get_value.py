#!/usr/bin/env python3
"""
Module for safely_get_value function
"""

from typing import Mapping, Any, TypeVar, Union

# Define a generic type variable
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary-like object
    
    Parameters:
    dct (Mapping): A dictionary-like object (could be a dict, OrderedDict, etc.)
    key (Any): The key to lookup in the dictionary
    default (T, optional): The default value to return if key is not found (default is None)
    
    Returns:
    Union[Any, T]: The value associated with the key if found, otherwise the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
