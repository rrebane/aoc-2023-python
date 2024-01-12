"""Tests for AoC 2, 2023: Cube Conundrum."""

# Standard library imports
import pathlib

# Third party imports
import aoc202302
import pytest

from aoc202302 import Color

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202302.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202302.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [(1, [[(3, Color.blue), (4, Color.red)], [(1, Color.red), (2, Color.green), (6, Color.blue)], [(2, Color.green)]]), (2, [[(1, Color.blue), (2, Color.green)], [(3, Color.green), (4, Color.blue), (1, Color.red)], [(1, Color.green), (1, Color.blue)]]), (3, [[(8, Color.green), (6, Color.blue), (20, Color.red)], [(5, Color.blue), (4, Color.red), (13, Color.green)], [(5, Color.green), (1, Color.red)]]), (4, [[(1, Color.green), (3, Color.red), (6, Color.blue)], [(3, Color.green), (6, Color.red)], [(3, Color.green), (15, Color.blue), (14, Color.red)]]), (5, [[(6, Color.red), (1, Color.blue), (3, Color.green)], [(2, Color.blue), (1, Color.red), (2, Color.green)]])]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202302.part1(example1) == 8


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202302.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202302.part2(example2) == ...
