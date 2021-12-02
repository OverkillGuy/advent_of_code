"""Day 1 solution to AoC 2021"""

from typing import List


def solution1(input_list: List[int]) -> int:
    """Solve day1 solution1 via zips

    >>> solution1([10, 20, 30, 40])
    3
    """
    off_by_one_list = input_list[1:]
    deltas = [i1 - i0 for i0, i1 in zip(input_list, off_by_one_list)]
    return sum([1 if delta > 0 else 0 for delta in deltas])


def solution2(input_list: List[int]) -> int:
    """Solve day1 solution2 via zips

    >>> solution2([607, 618, 618, 617, 647, 716, 769, 792])
    5
    """
    off_by_one_list = input_list[1:]
    off_by_two_list = input_list[2:]
    totals = [
        i0 + i1 + i2 for i0, i1, i2 in zip(input_list, off_by_one_list, off_by_two_list)
    ]
    return solution1(totals)
