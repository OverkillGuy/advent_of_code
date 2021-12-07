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
