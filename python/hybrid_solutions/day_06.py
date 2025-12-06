from typing import cast

import pyuiua

from models.aoc_solution import AOCSolution, Dataset, Part


class Day06(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 4277556, Dataset.DATA: 5552221122013},
        Part.PART_TWO: {Dataset.SAMPLE: 3263827, Dataset.DATA: 11371597126232},
    }

    def apply_op(self, op: str, nums: list[int]) -> int:
        """Reduce with the given operation"""
        return cast(int, pyuiua.eval("⨬/+/×=@*⊢", op, nums))

    def parse_lines(self, lines: list[str]) -> list[list[int]]:
        return [list(map(int, row.split())) for row in lines]

    def __post_init__(self) -> None:
        """Extract the rows of numbers and the operations"""
        *number_lines, ops = self.data.splitlines()

        parsed_rows = self.parse_lines(number_lines)
        self.number_rows = cast(list[list[int]], pyuiua.eval("⍉", parsed_rows))

        col_grid = cast(list[str], pyuiua.eval("⍚▽⊸≠@ ⍉", number_lines))
        col_lines = "\n".join(col_grid).split("\n\n")
        self.number_cols = self.parse_lines(col_lines)

        self.ops = ops.split()

    def part_one(self) -> int:
        """Apply the operation to each row in that column and take the sum"""
        total = 0
        for values, op in zip(self.number_rows, self.ops, strict=True):
            total += self.apply_op(op, values)
        return total

    def part_two(self) -> int:
        """Apply the operation against each column aligned to that operation and take the sum"""
        total = 0
        for values, op in zip(self.number_cols, self.ops, strict=True):
            total += self.apply_op(op, values)
        return total


if __name__ == "__main__":
    Day06().run()
