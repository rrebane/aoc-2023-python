"""AoC 2, 2023: Cube Conundrum."""

# Standard library imports
import pathlib
import sys

from enum import Enum

from parsimonious.grammar import Grammar, NodeVisitor


class Color(Enum):
    """Color."""
    red = 1
    green = 2
    blue = 3


class InputVisitor(NodeVisitor):
    """Parsimonious to Python data."""
    def visit_game(self, node, visited_children):
        _, game_id, _, game_sets, _ = visited_children
        return (game_id, game_sets)

    def visit_set(self, node, visited_children):
        draws, _ = visited_children
        return draws

    def visit_draw(self, node, visited_children):
        _, n_cubes, _, color = visited_children
        return (n_cubes, color)

    def visit_color(self, node, visited_children):
        return Color[node.text]

    def visit_integer(self, node, visited_children):
        return int(node.text)

    def generic_visit(self, node, visited_children):
        return visited_children or node


def parse_data(puzzle_input):
    """Parse input."""
    input_grammar = Grammar(
        r"""
        input = game+
        game = "Game " integer ": " set+ "\n"?
        set =  draw+ "; "?
        draw = ", "? integer " " color
        color = "red" / "green" / "blue"
        integer = ~r"[1-9][0-9]*"
        """
    )

    parsed_input = input_grammar.parse(puzzle_input)
    typed_input = InputVisitor().visit(parsed_input)

    return typed_input


def part1(data):
    """Solve part 1."""
    print(data)


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
