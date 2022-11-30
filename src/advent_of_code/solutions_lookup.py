"""Lookup table for Advent of Code solution functions"""

from typing import Callable, Dict

from advent_of_code import Day, Part, Year
from advent_of_code.aoc2021 import SOLUTIONS_2021

SOLUTIONS_LOOKUP: Dict[Year, Dict[Day, Dict[Part, Callable]]] = {
    2021: SOLUTIONS_2021,
}
"""Big map of solutions function, indexed by year->day->part"""
