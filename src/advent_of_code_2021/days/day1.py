"""Day 1 solution to AoC 2021"""


def solution1(input_list):
    """Solve day1 solution1 via zips

    >>> solution1([10, 20, 30, 40])
    3
    """
    off_by_one_list = input_list[1:]
    deltas = [i1 - i0 for i0, i1 in zip(input_list, off_by_one_list)]
    return sum([1 if delta > 0 else 0 for delta in deltas])
