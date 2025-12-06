from models.aoc_solution import AOCSolution, Dataset, Part

from functools import reduce
class Day06(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 4277556, Dataset.DATA: None},
        Part.PART_TWO: {Dataset.SAMPLE: None, Dataset.DATA: None},
    }

    def __post_init__(self) -> None:
        *number_lines, ops = self.data.splitlines()
        self.numbers = [[int(n) for n in row.split()] for row in number_lines]
        lookup = {
            "*": lambda a, b: a * b,
            "+": lambda a, b: a + b,
        }
        self.num_t = [[self.numbers[j][i] for j in range(len(number_lines))]for i in range(len(ops.split()))]
        self.ops = [lookup.get(op) for op in ops.split()]

    def part_one(self) -> int:
        """Solve part one."""
        total = 0
        for values, op in zip(self.num_t, self.ops):
            total += reduce(op, values)
        return total

    def part_two(self) -> int:
        """Solve part two."""
        pass


if __name__ == "__main__":
    Day06().run()
