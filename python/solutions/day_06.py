from functools import reduce
from typing import Callable, Iterable

from models.aoc_solution import AOCSolution, Dataset, Part


class Day06(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 4277556, Dataset.DATA: 5552221122013},
        Part.PART_TWO: {Dataset.SAMPLE: 3263827, Dataset.DATA: 11371597126232},
    }

    def parse_op(self, op: str) -> Callable[[int, int], int]:
        lookup: dict[str, Callable[[int, int], int]] = {
            "*": lambda a, b: a * b,
            "+": lambda a, b: a + b,
        }
        return lookup[op]

    def transpose[T](self, items: Iterable[Iterable[T]]) -> list[list[T]]:
        return list(map(list, zip(*items, strict=True)))

    def __post_init__(self) -> None:
        """Extract the rows of numbers and the operations"""
        *number_lines, ops = self.data.splitlines()
        transposed_number_grid = "\n".join(
            "".join(row).strip() for row in self.transpose(number_lines)
        )

        self.nums = self.transpose([[int(n) for n in row.split()] for row in number_lines])
        self.transposed_nums = [
            [int(row) for row in group.split()] for group in transposed_number_grid.split("\n\n")
        ]
        self.ops = [self.parse_op(op) for op in ops.split()]

    def part_one(self) -> int:
        """Apply the operation to each row in that column and take the sum"""
        total = 0
        for values, op in zip(self.nums, self.ops, strict=True):
            total += reduce(op, values)
        return total

    def part_two(self) -> int:
        """Apply the operation against each column aligned to that operation and take the sum"""
        total = 0
        for values, op in zip(self.transposed_nums, self.ops, strict=True):
            total += reduce(op, values)
        return total


if __name__ == "__main__":
    Day06().run()
