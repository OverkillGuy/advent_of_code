"""Day 1 solution to AoC 2022"""

from advent_of_code.input_conversion import newlines_to_integer_list

Calories = int
"""A single meal's calory content"""
ElfFood = list[Calories]
"""Meals carried by a single Elf """
FoodSupply = list[ElfFood]
"""The entirety of the food supply for all elves"""


def solution1(puzzle_input: FoodSupply) -> int:
    """Solve day1 solution1

    >>> solution1([[1000], [2000, 3000]])
    3
    """
    return 3


def read_food_supply(puzzle_input: str) -> FoodSupply:
    r"""Process the puzzle input into food

    >>> s="1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
    >>> read_food_supply(s)
    [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    """
    food_grouped: list[str] = puzzle_input.split("\n\n")
    return [newlines_to_integer_list(elf_food) for elf_food in food_grouped]


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day1 solution1"""
    return solution1(read_food_supply(puzzle_input))
