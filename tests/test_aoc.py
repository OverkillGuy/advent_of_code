"""Check aoc solutions for all days"""

import pytest

from advent_of_code.solutions_lookup import SOLUTIONS_LOOKUP, Day, Part, Year

SolutionCombination = tuple[Year, Day, Part]
"""A single solution, combination of Year+Day+Part"""

SOLUTIONS_LIST: list[SolutionCombination] = []
"""The entirety of all info about solutions, just the year/day/part numbers"""


for year, days_lookup in SOLUTIONS_LOOKUP.items():
    for day, parts in days_lookup.items():
        solutions = [(year, day, p) for p in parts]
        SOLUTIONS_LIST.extend(solutions)


@pytest.mark.parametrize("year,day,part", SOLUTIONS_LIST)
def test_solutions_with_input(year, day, part, shared_datadir):
    """Scenario Outline: Proving each solved day works on real input"""
    # Given an input file for day <day number> of <year number>
    # And the known solution for day <day number> part <part number> of <year number>
    # When I run the solution with input file of day <day number>
    d = f"{day:02d}"
    solution_func = SOLUTIONS_LOOKUP[year][day][part]
    input_file = shared_datadir / f"y{year}" / f"input{d}.txt"
    output_file = shared_datadir / f"y{year}" / f"output{d}_{part}.txt"
    if not input_file.exists():
        pytest.skip("No puzzle input to compute")
    with open(input_file) as fd:
        problem_input = fd.read()
    computed_answer = solution_func(problem_input)
    if not output_file.exists():
        pytest.skip(f"No reference output, but {computed_answer=}")
    # Then the answer is an integer
    assert type(computed_answer) == int, "An integer should be generated"
    # And the answer is equal to the known solution
    with open(output_file) as fd:
        expected_answer = int(fd.read().strip())
    assert (
        computed_answer == expected_answer
    ), "Did not compute the answer that was proven to work"
