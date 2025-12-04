from models.aoc_solution import AOCSolution, Dataset, Part
from functools import cached_property, cache

class Day04(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 13, Dataset.DATA: None},
        Part.PART_TWO: {Dataset.SAMPLE: None, Dataset.DATA: None},
    }

    def __post_init__(self):
        self.width = len(self.parsed_data[0])
        self.height = len(self.parsed_data)

    @cached_property
    def parsed_data(self):
        """Parse and return the input data."""
        return [[int(x == "@") for x in row] for row in self.data.splitlines()]

    @cache
    def count_nbrs(self, r: int, c: int) -> int:
        total = 0
        for y, x in [(r-1, c), (r+1,c), (r-1,c-1), (r+1,c+1), (r,c-1), (r,c+1), (r+1,c-1), (r-1,c+1)]:
            if y in range(self.height) and x in range(self.width):
                total += self.parsed_data[y][x]
        return total
    
    def part_one(self) -> int:
        """Solve part one."""
        valid = []
        for r in range(self.height):
            for c in range(self.width):
                if self.count_nbrs(r, c) < 4 and self.parsed_data[r][c]:
                    valid.append((r,c))

        return len(valid)


    def part_two(self) -> int:
        """Solve part two."""
        pass


if __name__ == "__main__":
    Day04().run()
