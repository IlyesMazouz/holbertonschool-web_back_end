#!/usr/bin/env python3
"""
annotating function paramaters and returning
values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in the input list
    """
    return [(i, len(i)) for i in lst]
