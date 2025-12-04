from models.aoc_solution import AOCSolution, Dataset, Part


class Day03(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 357, Dataset.DATA: 17316},
        Part.PART_TWO: {Dataset.SAMPLE: 3121910778619, Dataset.DATA: 171741365473332},
    }

    @property
    def parsed_data(self) -> list[list[int]]:
        """Return list of digits for each row"""
        return [[int(c) for c in row] for row in self.data.splitlines()]

    def best_number(self, row: list[int], length: int) -> int:
        """Get maximum subarray of given length from row whilst preserving order"""
        best: list[int] = []
        remaining = row
        for i in range(length):
            best_digit = max(remaining[: len(remaining) + i + 1 - length])
            best_index = remaining.index(best_digit)
            best.append(best_digit)
            remaining = remaining[best_index + 1 :]

        return int("".join(map(str, best)))

    def part_one(self) -> int:
        """Best 2 digit number"""
        return sum(self.best_number(r, 2) for r in self.parsed_data)

    def part_two(self) -> int:
        """Best 12 digit number"""
        return sum(self.best_number(r, 12) for r in self.parsed_data)


if __name__ == "__main__":
    Day03().run()
