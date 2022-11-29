"""Day 2 solution using Complex numbers for 2D vectors"""

from enum import Enum
from typing import Dict, List, NamedTuple

from advent_of_code.input_conversion import to_string_list


class Direction(str, Enum):
    """Sonar directions"""

    FORWARD = "forward"
    DOWN = "down"
    UP = "up"


DIRECTIONS_VECTOR: Dict[str, complex] = {
    Direction.FORWARD: 1 + 0j,
    Direction.DOWN: 0 + 1j,
    Direction.UP: 0 - 1j,
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


class Pose(NamedTuple):
    """Aggregate of position, depth and aim"""

    position: int
    depth: int
    aim: int


def apply_movement_aim(before: Pose, movement: str) -> Pose:
    """Apply a single movement to a Pose

    >>> apply_movement_aim(Pose(position=0, depth=0, aim=0), "forward 5")
    Pose(position=5, depth=0, aim=0)
    >>> apply_movement_aim(Pose(position=5, depth=0, aim=0), "down 5")
    Pose(position=5, depth=0, aim=5)
    >>> apply_movement_aim(Pose(position=5, depth=0, aim=5), "forward 8")
    Pose(position=13, depth=40, aim=5)
    >>> apply_movement_aim(Pose(position=13, depth=40, aim=5), "up 3")
    Pose(position=13, depth=40, aim=2)
    >>> apply_movement_aim(Pose(position=13, depth=40, aim=2), "down 8")
    Pose(position=13, depth=40, aim=10)
    >>> apply_movement_aim(Pose(position=13, depth=40, aim=10), "forward 2")
    Pose(position=15, depth=60, aim=10)
    """
    direction, distance_str = movement.split(" ")
    distance = int(distance_str)

    if direction == Direction.DOWN:
        return Pose(before.position, before.depth, before.aim + distance)
    if direction == Direction.UP:
        return Pose(before.position, before.depth, before.aim - distance)
    if direction == Direction.FORWARD:
        return Pose(
            position=before.position + distance,
            depth=before.depth + before.aim * distance,
            aim=before.aim,
        )
    else:
        raise KeyError(f"Bad direction: '{direction}'")


def solution2(input_list: List[str]) -> int:
    """Solve day2 solution2

    >>> d = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    >>> solution2(d)
    900
    """
    pose = Pose(position=0, depth=0, aim=0)
    for movement in input_list:
        pose = apply_movement_aim(pose, movement)
    return pose.position * pose.depth


def solve1_stringlist(input_str: str) -> int:
    """Convert list to proper format and solve day2 solution1"""
    return solution1(to_string_list(input_str))


def solve2_stringlist(input_str: str) -> int:
    """Convert list to proper format and solve day2 solution2"""
    return solution2(to_string_list(input_str))
