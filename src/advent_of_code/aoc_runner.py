"""CLI dispatcher to run a specific day's solutions"""

import argparse
import sys

from advent_of_code.solutions_lookup import SOLUTIONS_LOOKUP


def parse_arguments(arguments: list[str]) -> argparse.Namespace:
    """Parse generic arguments, given as parameters"""
    parser = argparse.ArgumentParser("aoc", description="Advent of Code runner")
    parser.add_argument("-y", "--year", type=int, help="What year to use for problem")
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
    parser.set_defaults(solution2=False, year=2023)
    return parser.parse_args(arguments)


def cli():
    """Run the aoc cli"""
    args = parse_arguments(sys.argv[1:])
    if args.year not in SOLUTIONS_LOOKUP:
        print(f"Year {args.year} hasn't got any solutions", file=sys.stderr)
        sys.exit(1)
    YEAR_SOLUTIONS_LOOKUP = SOLUTIONS_LOOKUP[args.year]
    if args.day not in YEAR_SOLUTIONS_LOOKUP:
        print(
            f"Day {args.day} isn't solved right now for year {args.year}",
            file=sys.stderr,
        )
        sys.exit(1)
    day_selected = YEAR_SOLUTIONS_LOOKUP[args.day]
    solution_selected = 2 if args.solution2 else 1
    if solution_selected not in day_selected:
        print(
            f"Day {args.day} problem {solution_selected} isn't solved right now "
            f"for year {args.year}",
            file=sys.stderr,
        )
        sys.exit(1)
    solution = day_selected[solution_selected]
    answer = solution(args.input_file.read())
    print(answer)
