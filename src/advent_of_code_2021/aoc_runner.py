"""CLI dispatcher to run a specific day's solutions"""

import argparse
import sys

from advent_of_code_2021.days import day0

DAYS = {
    # Dummy day0 with real function to run tests
    0: {1: day0.solution1, 2: day0.solution2},
    # Fake day29 with just no solution2
    29: {1: lambda x: True},
}


def parse_arguments(arguments):
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


def cli():
    """Run the aoc cli"""
    args = parse_arguments(sys.argv[1:])
    if args.day not in DAYS:
        print(f"Day {args.day} isn't solved right now", file=sys.stderr)
        sys.exit(1)
    day_selected = DAYS[args.day]
    solution_selected = 2 if args.solution2 else 1
    if solution_selected not in day_selected:
        print(
            f"Day {args.day} problem {solution_selected} isn't solved right now",
            file=sys.stderr,
        )
        sys.exit(1)
    solve_function = day_selected[solution_selected]
    input_list = [int(i) for i in args.input_file.readlines()]
    print(solve_function(input_list))
