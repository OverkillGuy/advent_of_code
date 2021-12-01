
.PHONY: all
all: install lint test build

.PHONY: install
install:
	poetry install


.PHONY: lint
lint:  # Use all linters on all files (not just staged for commit)
	pre-commit run --all --all-files

.PHONY: test
test:
	poetry run pytest \
		--cov=advent_of_code_2021 \
		--cov-report=term \
		--cov-report=xml:test_results/coverage.xml \
		--junit-xml=test_results/results.xml

.PHONY: build
build:
	poetry build


# Less commonly used commands

# Generate a pip-compatible requirements.txt
# From the poetry.lock. Mostly for CI use.
.PHONY: export-requirements
export-requirements:
	poetry -o requirements.txt


# Install poetry from pip
# IMPORTANT: Make sure "pip" resolves to a virtualenv
# Or that you are happy with poetry installed system-wide
.PHONY: install-poetry
install-poetry:
	pip install poetry

# Ensure Poetry will generate virtualenv inside the git repo /.venv/
# rather than in a centralized location. This makes it possible to
# manipulate venv more simply
.PHONY: poetry-venv-local
poetry-venv-local:
	poetry config virtualenvs.in-project true

# Delete the virtualenv to clean dependencies
# Useful when switching to a branch with less dependencies
# Requires the virtualenv to be local (see "poetry-venv-local")
poetry-venv-nuke:
	find .venv -delete
