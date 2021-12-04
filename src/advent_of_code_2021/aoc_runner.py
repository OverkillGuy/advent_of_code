"""CLI dispatcher to run a specific day's solutions"""

import argparse
import sys
from typing import IO, Callable, List

from advent_of_code_2021.solutions_lookup import SOLUTION_LOOKUP_DAYS


def parse_arguments(arguments: List[str]) -> argparse.Namespace:
    """Parse generic arguments, given as parameters"""
    parser = argparse.ArgumentParser("aoc", description="Advent of Code runner 2021")
    parser.add_argument(
        "-d", "--day", type=int, required=True, help="What day's problem to solve"
    )
    parser.add_argument(
        "-f",
        "--input-file",
        type=argparse.FileType("r"),
        required=True,
        help="Input file for that day",
    )
    parser.add_argument("-1", "--solution1", dest="solution2", action="store_false")
    parser.add_argument("-2", "--solution2", dest="solution2", action="store_true")
    parser.set_defaults(solution2=False)
    return parser.parse_args(arguments)


def solve(input_fd: IO, solution: Callable) -> int:
    """Compute the solution on a given input file"""
    return solution(input_fd.readlines())


def cli():
    """Run the aoc cli"""
    args = parse_arguments(sys.argv[1:])
    if args.day not in SOLUTION_LOOKUP_DAYS:
        print(f"Day {args.day} isn't solved right now", file=sys.stderr)
        sys.exit(1)
    day_selected = SOLUTION_LOOKUP_DAYS[args.day]
    solution_selected = 2 if args.solution2 else 1
    if solution_selected not in day_selected:
        print(
            f"Day {args.day} problem {solution_selected} isn't solved right now",
            file=sys.stderr,
        )
        sys.exit(1)
    answer = solve(input_fd=args.input_file, solution=day_selected[solution_selected])
    print(answer)
