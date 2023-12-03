"""Basic tests of advent of code."""

import subprocess

import pytest

CMD_ROOT = ["poetry", "run", "aoc"]


def test_cli_noarg_errors():
    """Scenario: AOC CLI without args shows help"""
    # Given the installed CLI
    # When I invoke "poetry run aoc --help"
    cmd = subprocess.run(CMD_ROOT + ["--help"], capture_output=True, text=True)
    # Then the exit code is OK
    assert cmd.returncode == 0, "CLI help shouldn't error out"
    # And output contains help
    assert "usage" in cmd.stdout, "CLI should show help when requested"


@pytest.fixture
def dummy_input(tmp_path):
    """Arbitrary puzzle input file to help run day0 mock-solution"""
    file_name = "dummy.txt"
    with open(tmp_path / file_name, "w") as fd:
        fd.write("\n".join(["10", "20", "30"]))
    return tmp_path / file_name


def test_cli_day0_ok(dummy_input):
    """Scenario: CLI solve runs OK on mock-day 0"""
    # Given a dummy input file
    # When I invoke "poetry run aoc --day 0 --input-file dummy.txt"
    cmd = CMD_ROOT + ["--day", "0", "--year", "2021", "--input-file", str(dummy_input)]
    day0 = subprocess.run(cmd, capture_output=True, text=True)
    # Then the exit code is OK
    print(f"Errors: '{day0.stderr}'")
    print(f"Info: '{day0.stdout}'")
    assert day0.returncode == 0, "Day0 should run OK"
    # And output gives number "10"
    assert int(day0.stdout.strip()) == 10, "Output for day0 should give '10' back"


def test_cli_day0_solution_ok(dummy_input):
    """Scenario: CLI solution 2 runs OK on mock-day 0"""
    # Given a dummy input file
    # When I invoke "poetry run aoc --solution2 --day 0 --input-file dummy.txt"
    cmd = CMD_ROOT + [
        "--solution2",
        "--year",
        "2021",
        "--day",
        "0",
        "--input-file",
        str(dummy_input),
    ]
    day0 = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Errors: '{day0.stderr}'")
    print(f"Info: '{day0.stdout}'")
    # Then the exit code is OK
    assert day0.returncode == 0, "Day0 solution 2 should run OK"
    # And output gives number "20"
    assert (
        int(day0.stdout.strip()) == 20
    ), "Output for day0 solution2 should give '20' back"


def test_day30_nosolution_fails(dummy_input):
    """Scenario: Asking for a day without solution fails"""
    # Given a dummy input file
    # When I invoke "poetry run aoc --day 30 --input-file dummy.txt"
    cmd = CMD_ROOT + [
        "--day",
        "30",
        "--input-file",
        str(dummy_input),
    ]
    day30 = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Errors: '{day30.stderr}'")
    print(f"Info: '{day30.stdout}'")
    # Then the exit code is nonzero
    assert day30.returncode != 0, "Asking day30 when missing solution should error out"
    # And output is an error
    assert (
        "isn't solved right now" in day30.stderr
    ), "Output for day0 solution2 should give '20' back"


def test_day30_nosolution2_fails(dummy_input):
    """Scenario: Asking for a day's problem2 without solution2 fails"""
    # Given a dummy input file
    # When I invoke "poetry run aoc --solution2 --day 30 --input-file dummy.txt"
    cmd = CMD_ROOT + [
        "--year",
        "2021",
        "--solution2",
        "--day",
        "29",
        "--input-file",
        str(dummy_input),
    ]
    day29_sol2 = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Errors: '{day29_sol2.stderr}'")
    print(f"Info: '{day29_sol2.stdout}'")
    # Then the exit code is nonzero
    assert day29_sol2.returncode != 0, "Asking solution2 when missing should error out"
    # And output is an error
    assert (
        "isn't solved right now" in day29_sol2.stderr
    ), "Output for day0 solution2 should give '20' back"
