"""Day7 crab alignment"""

from collections import Counter
from typing import List

from advent_of_code_2021.input_conversion import csv_to_integer_list

sample_crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def cost_alignment(crabs: List[int], target_position: int) -> int:
    """Calculate the alignment cost of a position

    >>> cost_alignment(sample_crabs, 1)
    41
    >>> cost_alignment(sample_crabs, 3)
    39
    >>> cost_alignment(sample_crabs, 10)
    71
    """
    return sum([abs(position - target_position) for position in crabs])


def align_crabs(crabs: List[int]) -> int:
    """Find best alignment for crabs

    >>> align_crabs(sample_crabs)
    37
    """
    crab_position_bins = Counter(crabs)
    max_position = max(crab_position_bins.keys())
    # Heuristic for max cost: largest distance (max - 0) = max
    # for each crab (hence len(crabs)), twice, for good measure
    best_cost: int = max_position * len(crabs) * 2
    # best_position: int = -1
    for position in range(max_position + 1):
        cost = cost_alignment(crabs, position)
        if cost < best_cost:
            # best_position = position
            best_cost = cost
    return best_cost


def solution1(input_str: str) -> int:
    """Solve day 7 part 1"""
    return align_crabs(csv_to_integer_list(input_str))


def cost_alignment2(crabs: List[int], target_position: int) -> int:
    """Calculate the alignment cost of a position for part 2

    >>> cost_alignment2(sample_crabs, 5)
    168
    >>> cost_alignment2(sample_crabs, 2)
    206
    """
    return sum(sum_till_n(abs(position - target_position)) for position in crabs)


def sum_till_n(n: int) -> int:
    """Calculate the sum of numbers from 1 to n included

    >>> sum_till_n(1)
    1
    >>> sum_till_n(2)
    3
    >>> sum_till_n(5)
    15
    """
    return (n * (n + 1)) // 2


def align_crabs2(crabs: List[int]) -> int:
    """Find best alignment for crabs using second part calculation

    >>> align_crabs2(sample_crabs)
    168
    """
    crab_position_bins = Counter(crabs)
    max_position = max(crab_position_bins.keys())
    # Upper boundary of sum_till_n cost: x ^ 2 > (x * (x+1)) / 2 > (x ** 2 ) / 2
    # Heuristic for max cost: for each crab, take upper boundary of dist
    best_cost: int = (max_position ** 2) * len(crabs)
    # best_position: int = -1
    for position in range(max_position + 1):
        cost = cost_alignment2(crabs, position)
        if cost < best_cost:
            # best_position = position
            best_cost = cost
    return best_cost


def solution2(input_str: str) -> int:
    """Solve day 7 part 2"""
    return align_crabs2(csv_to_integer_list(input_str))
