"""Day 2 solution using Complex numbers for 2D vectors"""

from typing import Dict, List

DIRECTIONS_VECTOR: Dict[str, complex] = {
    "forward": 1 + 0j,
    "down": 0 + 1j,
    "up": 0 - 1j,
}


def follow_directions(input_list: List[str]) -> complex:
    """Follow given directions, returning end position

    >>> d = ["forward 5", "down 5", "forward 8","up 3", "down 8", "forward 2"]
    >>> follow_directions(d)
    (15+10j)
    """
    position = 0 + 0j
    for x in input_list:
        direction, distance = x.split(" ")
        position += DIRECTIONS_VECTOR[direction] * int(distance)
    return position


def solution1(input_list: List[str]) -> int:
    """Solve day2 solution1

    >>> solution1(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"])
    150
    """
    position = follow_directions(input_list)
    return int(position.real * position.imag)
