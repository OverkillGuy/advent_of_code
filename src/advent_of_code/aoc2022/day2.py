"""Day 2 solution to AoC 2022"""

from enum import Enum
from typing import Literal, Optional, Union

OpponentMove = Literal["A", "B", "C"]
MyMove = Literal["X", "Y", "Z"]

Moves = Union[OpponentMove, MyMove]

Strategy = tuple[OpponentMove, MyMove]

StrategyGuide = list[Strategy]

Score = int


SAMPLE_INPUT = """A Y
B X
C Z"""

SAMPLE_GUIDE: StrategyGuide = [("A", "Y"), ("B", "X"), ("C", "Z")]


class Shape(Enum):
    """A hand move for one side of rock-paper-scissors

    The value of the enum is the value of the shape
    """

    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def from_opponent(cls, move: OpponentMove):
        """Translate an OpponentMove to Shape"""
        lookup = {"A": cls.ROCK, "B": cls.PAPER, "C": cls.SCISSORS}
        return lookup[move]

    @classmethod
    def from_mine(cls, move: MyMove):
        """Translate MyMove to Shape"""
        lookup = {"X": cls.ROCK, "Y": cls.PAPER, "Z": cls.SCISSORS}
        return lookup[move]


WINS_AGAINST: dict[Shape, Shape] = {
    Shape.SCISSORS: Shape.ROCK,
    Shape.ROCK: Shape.PAPER,
    Shape.PAPER: Shape.SCISSORS,
}

# Reversing the map of winning moves
LOSE_AGAINST = {v: k for k, v in WINS_AGAINST.items()}


def play(opponent: Shape, mine: Shape) -> Optional[bool]:
    """Play a round of Rock Paper Scissors

    Returns True if I win, False if I lose, None if draw

    >>> play(Shape.ROCK, Shape.PAPER)  # My paper wins over their rock
    True
    >>> play(Shape.SCISSORS, Shape.PAPER)
    False
    >>> play(Shape.SCISSORS, Shape.SCISSORS)
    >>> play(Shape.PAPER, Shape.ROCK)
    False
    """
    if opponent == mine:
        return None
    # dict Value wins against dict key
    return WINS_AGAINST[opponent] == mine


def score_round(opponent: Shape, mine: Shape) -> Score:
    """Compute the integer score of the round

    >>> score_round(Shape.ROCK, Shape.PAPER)
    8
    >>> score_round(Shape.PAPER, Shape.ROCK)
    1
    >>> score_round(Shape.SCISSORS, Shape.SCISSORS)
    6
    """
    outcome_lookup = {None: 3, False: 0, True: 6}
    who_wins = play(opponent, mine)
    outcome_score = outcome_lookup[who_wins]
    shape_score = mine.value
    return shape_score + outcome_score


def solution1(puzzle_input: StrategyGuide) -> int:
    """Solve day2 part 1

    >>> solution1(SAMPLE_GUIDE)
    15
    """
    acc = 0
    for opponent, mine in puzzle_input:
        opp_shape, my_shape = Shape.from_opponent(opponent), Shape.from_mine(mine)
        acc += score_round(opp_shape, my_shape)
    return acc


def solution2(puzzle_input) -> int:
    """Solve day2 part 2

    >>> solution2(SAMPLE_GUIDE)
    12
    """
    acc = 0
    for opponent, result in puzzle_input:
        opp_shape = Shape.from_opponent(opponent)
        my_shape_lookup = {
            "X": LOSE_AGAINST[opp_shape],
            "Y": opp_shape,
            "Z": WINS_AGAINST[opp_shape],
        }
        my_shape = my_shape_lookup[result]
        acc += score_round(opp_shape, my_shape)
    return acc


def read_puzzle_input(puzzle_input: str) -> StrategyGuide:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT) == SAMPLE_GUIDE
    True
    """
    # Type ignored due to Mypy issue: puzzle_input str needs coerced into OpponentMove,
    # but can't find a way to express it! We _know_ the strings have these constraints!
    return [tuple(line.split()) for line in puzzle_input.splitlines()]  # type:ignore


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
