"""Convert the input's string list to useful format"""

from typing import List


def to_integer_list(input_list: List[str]) -> List[int]:
    """Convert a list of string to a list of integers

    >>> to_integer_list(["1", "2", "3"])
    [1, 2, 3]
    """
    return [int(i) for i in input_list]
