"""Day6 fish reproduction"""

from collections import defaultdict
from copy import copy
from typing import Dict, List, Tuple

from advent_of_code.input_conversion import csv_to_integer_list

FishTimer = int
FishList = List[FishTimer]


sample_fishes: FishList = [3, 4, 3, 1, 2]


def breed(fish_timer: FishTimer) -> Tuple[FishTimer, bool]:
    """Breed a single fish for one round, signaling new fish

    >>> breed(3)
    (2, False)
    >>> breed(2)
    (1, False)
    >>> breed(1)
    (0, False)
    >>> breed(0)
    (6, True)
    >>> breed(6)
    (5, False)
    """
    decreased_timer = fish_timer - 1
    if decreased_timer < 0:
        new_fish = True
        decreased_timer = 6
    else:
        new_fish = False
    return (decreased_timer, new_fish)


def breed_rounds(fish_list: FishList, number_rounds: int) -> FishList:
    """Apply number_rounds of breeding to fishes, returning their current breed time

    >>> breed_rounds(sample_fishes, 1)
    [2, 3, 2, 0, 1]
    >>> breed_rounds(sample_fishes, 2)
    [1, 2, 1, 6, 0, 8]
    >>> breed_rounds(sample_fishes, 3)
    [0, 1, 0, 5, 6, 7, 8]
    >>> breed_rounds(sample_fishes, 4)
    [6, 0, 6, 4, 5, 6, 7, 8, 8]
    >>> breed_rounds(sample_fishes, 5)
    [5, 6, 5, 3, 4, 5, 6, 7, 7, 8]
    >>> breed_rounds(sample_fishes,  6)
    [4, 5, 4, 2, 3, 4, 5, 6, 6, 7]
    >>> breed_rounds(sample_fishes, 7)
    [3, 4, 3, 1, 2, 3, 4, 5, 5, 6]
    >>> breed_rounds(sample_fishes, 8)
    [2, 3, 2, 0, 1, 2, 3, 4, 4, 5]
    >>> breed_rounds(sample_fishes, 9)
    [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 8]
    >>> breed_rounds(sample_fishes, 10)
    [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8]
    >>> breed_rounds(sample_fishes, 11)
    [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 7, 8, 8, 8]
    >>> breed_rounds(sample_fishes, 12)
    [5, 6, 5, 3, 4, 5, 6, 0, 0, 1, 5, 6, 7, 7, 7, 8, 8]
    >>> breed_rounds(sample_fishes, 13)
    [4, 5, 4, 2, 3, 4, 5, 6, 6, 0, 4, 5, 6, 6, 6, 7, 7, 8, 8]
    >>> breed_rounds(sample_fishes, 14)
    [3, 4, 3, 1, 2, 3, 4, 5, 5, 6, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8]
    >>> breed_rounds(sample_fishes, 15)
    [2, 3, 2, 0, 1, 2, 3, 4, 4, 5, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7]
    >>> breed_rounds(sample_fishes, 16)
    [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 8]
    >>> breed_rounds(sample_fishes, 17)
    [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7, 8]
    >>> breed_rounds(sample_fishes, 18)
    [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]
    >>> len(breed_rounds(sample_fishes, 80))
    5934
    """
    fishes = copy(fish_list)
    for _ in range(number_rounds):
        new_fishes: FishList = []
        for fish_index, fish_timer in enumerate(fishes):
            next_fish, create_new_fish = breed(fish_timer)
            fishes[fish_index] = next_fish
            if create_new_fish:
                new_fishes.append(8)
        fishes.extend(new_fishes)
    return fishes


def solution1(input_str: str) -> int:
    """Solve day6 problem 1"""
    input_list: FishList = [int(i) for i in input_str.strip().split(",")]
    return len(breed_rounds(input_list, 80))


def breed_bins(start_fishes: FishList, rounds: int) -> int:
    """Breed fishes by aggregating them as bins

    >>> breed_bins(sample_fishes, 80)
    5934
    >>> breed_bins(sample_fishes, 256)
    26984457539
    """
    fish_bin_counter: Dict[FishTimer, int] = defaultdict(int)
    for index in start_fishes:
        fish_bin_counter[index] += 1
    for _round in range(rounds):
        reset_fishes = fish_bin_counter[0]
        for i in range(9):
            if i == 6:  # 0 resets themselves to 6
                fish_bin_counter[i] = fish_bin_counter[i + 1] + reset_fishes
            elif i == 8:  # resets add fresh fishes
                fish_bin_counter[i] = reset_fishes
            else:  # otherwise, just shift 1 down
                fish_bin_counter[i] = fish_bin_counter[i + 1]
    return sum(fish_bin_counter.values())


def solution2(input_str: str) -> int:
    """Solve day6 problem 2"""
    return breed_bins(csv_to_integer_list(input_str), 256)
