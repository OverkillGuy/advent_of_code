# advent_of_code_2021

Solving Advent of Code 2021 with Python

Requires Python 3.8


## Usage

Run the per-day scripts with your own custom input:

	poetry run aoc --help
	poetry run aoc --day 1 --input-file my_input1.txt
	poetry run aoc --day 2 --solution2 --input-file my_input1.txt
	poetry run aoc -d 3 -2 -i my_input1.txt

## Development

### Python setup

This repository uses Python3.8, using
[Poetry](https://python-poetry.org) as package manager to define a
Python package inside `src/advent_of_code_2021/`.

`poetry` will create virtual environments if needed, fetch
dependencies, and install them for development.


For ease of development, a `Makefile` is provided, use it like this:

	make  # equivalent to "make all" = install lint test build
	# run only specific tasks:
	make install
	make lint
	make test
	# Combine tasks:
	make install test

Once installed, the module's code can now be reached through running
Python in Poetry:

	$ poetry run python
	>>> import advent_of_code_2021
	>>> print(advent_of_code_2021.version)
	"0.1.0"

This codebase uses [pre-commit](https://pre-commit.com) to run linting
tools like `flake8`. Use `pre-commit install` to install git
pre-commit hooks to force running these checks before any code can be
committed, use `make lint` to run these manually. Testing is provided
by `pytest` separately in `make test`.


### Testing

With the development tools set up, run pytest to see test results:

	pytest
