"""Check aoc solutions for all days"""

from typing import List, Tuple

import pytest

from advent_of_code.solutions_lookup import SOLUTION_LOOKUP_2021DAYS

SOLVED_DAYS_AND_PARTS = [
    (d, list(p.keys())) for d, p in SOLUTION_LOOKUP_2021DAYS.items()
]
SOLUTION_COMBOS: List[Tuple[int, int]] = []
for day, parts in SOLVED_DAYS_AND_PARTS:
    SOLUTION_COMBOS.extend((day, p) for p in parts)


@pytest.mark.parametrize("day,part", SOLUTION_COMBOS)
def test_solutions_with_input(day, part, shared_datadir):
    """Scenario Outline: Proving each solved day works on real input"""
    # Given an input file for day <day number>
    # And the known solution for day <day number> part <part number>
    # When I run the solution with input file of day <day number>
    solution_func = SOLUTION_LOOKUP_2021DAYS[day][part]
    d = f"{day:02d}"
    with open(shared_datadir / "y2021" / f"input{d}.txt") as fd:
        problem_input = fd.read()
    computed_answer = solution_func(problem_input)
    # Then the answer is an integer
    assert type(computed_answer) == int, "An integer should be generated"
    # And the answer is equal to the known solution
    with open(shared_datadir / "y2021" / f"output{d}_{part}.txt") as fd:
        expected_answer = int(fd.read().strip())
    assert (
        computed_answer == expected_answer
    ), "Did not compute the answer that was proven to work"
