from models.aoc_solution import AOCSolution, Dataset, Part


class Day03(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 357, Dataset.DATA: 17316},
        Part.PART_TWO: {Dataset.SAMPLE: 3121910778619, Dataset.DATA: 171741365473332},
    }

    @property
    def parsed_data(self) -> list[list[int]]:
        """Parse and return the input data."""
        return [[int(c) for c in row] for row in self.data.splitlines()]

    def best_number(self, row: list[int], length: int) -> int:
        best = [0] * length
        rowlen = len(row)
        i = 0
        for i, x in enumerate(row):
            for j, y in enumerate(best):
                if x > y and i < rowlen - (length - 1 - j):
                    best[j] = x
                    for u in range(j + 1, length):
                        best[u] = 0
                    break
        return int("".join(map(str, best)))

    def part_one(self) -> int:
        """Solve part one."""
        return sum(self.best_number(r, 2) for r in self.parsed_data)

    def part_two(self) -> int:
        """Solve part two."""
        return sum(self.best_number(r, 12) for r in self.parsed_data)


if __name__ == "__main__":
    Day03().run()
