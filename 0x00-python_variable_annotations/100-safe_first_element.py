#!/usr/bin/env python3
"""task 100"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe_first_element function"""
    if lst:
        return lst[0]
    else:
        return None
