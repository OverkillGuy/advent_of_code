# Advent of Code

Solving Advent of Code with Python

Requires Python >=3.10


## Usage

Run the per-day scripts with your own custom input:

	poetry run aoc --help
	poetry run aoc --day 1 --input-file my_input1.txt
	poetry run aoc --day 2 --solution2 --input-file my_input1.txt
	poetry run aoc -d 3 -2 -i my_input1.txt

See the `features/` folder for an overview of the CLI and testing strategy in plain english ([Gherkin](https://cucumber.io/docs/gherkin/reference/)).

### Run the command

Install the module first:

    make install
    # or
    poetry install

Then inside the virtual environment, launch the command:

    # Run single command inside virtualenv
    poetry run advent-of-code

    # or
    # Load the virtualenv first
    poetry shell
    # Then launch the command, staying in virtualenv
    advent-of-code

## Development

### Python setup

This repository uses Python3.10, using
[Poetry](https://python-poetry.org) as package manager to define a
Python package inside `src/advent_of_code/`.

`poetry` will create virtual environments if needed, fetch
dependencies, and install them for development.


For ease of development, a `Makefile` is provided, use it like this:

	make  # equivalent to "make all" = install lint docs test build
	# run only specific tasks:
	make install
	make lint
	make test
	# Combine tasks:
	make install test

Once installed, the module's code can now be reached through running
Python in Poetry:

	$ poetry run python
	>>> from advent_of_code import main
	>>> main("blabla")


This codebase uses [pre-commit](https://pre-commit.com) to run linting
tools like `flake8`. Use `pre-commit install` to install git
pre-commit hooks to force running these checks before any code can be
committed, use `make lint` to run these manually. Testing is provided
by `pytest` separately in `make test`.

### Documentation

Documentation is generated via [Sphinx](https://www.sphinx-doc.org/en/master/),
using the cool [myst_parser](https://myst-parser.readthedocs.io/en/latest/)
plugin to support Markdown files like this one.

Other Sphinx plugins provide extra documentation features, like the recent
[AutoAPI](https://sphinx-autoapi.readthedocs.io/en/latest/index.html) to
generate API reference without headaches.

To build the documentation, run

    # Requires the project dependencies provided by "make install"
    make docs
	# Generates docs/build/html/

To browse the website version of the documentation you just built, run:

    make docs-serve

And remember that `make` supports multiple targets, so you can generate the
documentation and serve it:

    make docs docs-serve


### Templated repository

This repo was created by the cookiecutter template available at
https://github.com/OverkillGuy/python-template, using commit hash: `5c882f2e22311a2307263d14877c8229a2ed6961`.
