"""Basic tests of my_lovely_project."""

import subprocess


def test_cli_noarg_errors():
    """Scenario: AOC CLI without args shows help"""
    # Given the installed CLI
    # When I invoke "poetry run aoc --help"
    cmd = subprocess.run(
        ["poetry", "run", "aoc", "--help"], capture_output=True, text=True
    )
    # Then the exit code is OK
    assert cmd.returncode == 0, "CLI help shouldn't error out"
    # And output contains help
    assert "usage" in cmd.stdout, "CLI should show help when requested"
