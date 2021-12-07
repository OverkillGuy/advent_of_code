"""Convert the input's string list to useful format"""

from typing import List

sample_string = """1
2
3"""


def newlines_to_integer_list(input_str: str) -> List[int]:
    """Convert a newline-delimited string to a list of integers

    >>> newlines_to_integer_list(sample_string)
    [1, 2, 3]
    """
    return [int(i) for i in input_str.strip().split("\n")]


def to_string_list(input_str: str) -> List[str]:
    """Convert a newline-delimited string to a list of strings

    >>> to_string_list(sample_string)
    ['1', '2', '3']
    """
    return input_str.rstrip().split("\n")
