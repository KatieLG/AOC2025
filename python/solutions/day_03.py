from models.aoc_solution import AOCSolution, Dataset, Part


class Day03(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 357, Dataset.DATA: 17316},
        Part.PART_TWO: {Dataset.SAMPLE: None, Dataset.DATA: None},
    }

    @property
    def parsed_data(self):
        """Parse and return the input data."""
        return [[int(c) for c in row] for row in self.data.splitlines()]

    def best_number(self, row: list[int]) -> int:
        max_f = 0
        max_s = 0
        rowlen = len(row)
        for i, x in enumerate(row):
            if x > max_f and i < rowlen - 1:
                max_f = x
                max_s = row[i+1]
            elif x > max_s:
                max_s = x
        return int(f"{max_f}{max_s}")
    
    def part_one(self) -> int:
        """Solve part one."""
        best = [self.best_number(r) for r in self.parsed_data]
        return sum(best)

    def part_two(self) -> int:
        """Solve part two."""
        pass


if __name__ == "__main__":
    Day03().run()
