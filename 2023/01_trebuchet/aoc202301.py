"""AoC 1, 2023: Trebuchet?!."""

# Standard library imports
import math
import pathlib
import sys


NUMBER_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split()


def find_numeric_char(line, first=True):
    for idx, ch in enumerate(line if first else line[::-1]):
        if ch.isnumeric():
            return (idx if first else len(line) - idx - 1, int(ch))
    return (math.inf if first else -math.inf, None)


def find_numeric_word(line, first=True):
    idx = math.inf if first else -math.inf
    num = None

    for word_num, word in enumerate(NUMBER_WORDS):
        found_idx = -1
        while (found_idx := line.find(word, found_idx + 1)) != -1:
            if first and found_idx < idx:
                idx = found_idx
                num = word_num
                break

            if not first and found_idx > idx:
                idx = found_idx
                num = word_num

    return (idx, num)


def part1(data):
    """Solve part 1."""
    result = []

    for line in data:
        _, first = find_numeric_char(line)
        _, last = find_numeric_char(line, False)
        result.append(int(f"{first}{last}"))

    return sum(result)


def part2(data):
    """Solve part 2."""
    result = []

    for line in data:
        first_char_idx, first_char = find_numeric_char(line)
        last_char_idx, last_char = find_numeric_char(line, False)
        first_word_idx, first_word = find_numeric_word(line)
        last_word_idx, last_word = find_numeric_word(line, False)

        first = first_char if first_char_idx < first_word_idx else first_word
        last = last_char if last_char_idx > last_word_idx else last_word

        result.append(int(f"{first}{last}"))

    return sum(result)


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
