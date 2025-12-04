from models.aoc_solution import AOCSolution, Dataset, Part


class Day04(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 13, Dataset.DATA: 1437},
        Part.PART_TWO: {Dataset.SAMPLE: 43, Dataset.DATA: 8765},
    }

    def __post_init__(self) -> None:
        self.width = len(self.parsed_data[0])
        self.height = len(self.parsed_data)
        self.grid = self.parsed_data

    @property
    def parsed_data(self) -> list[list[int]]:
        """Parse and return the input data."""
        return [[int(x == "@") for x in row] for row in self.data.splitlines()]

    def count_nbrs(self, r: int, c: int) -> int:
        total = 0
        nbrs = [(r + i, c + j) for i in range(-1, 2) for j in range(-1, 2) if not i==j==0]
        for y, x in nbrs:
            if y in range(self.height) and x in range(self.width):
                total += self.grid[y][x]
        return total

    def removable(self) -> list[tuple[int, int]]:
        valid = []
        for r in range(self.height):
            for c in range(self.width):
                if self.count_nbrs(r, c) < 4 and self.grid[r][c]:
                    valid.append((r, c))

        return valid

    def part_one(self) -> int:
        """Solve part one."""
        return len(self.removable())

    def part_two(self) -> int:
        """Solve part two."""
        total = 0
        while True:
            removable = self.removable()
            if len(removable):
                for r, c in removable:
                    self.grid[r][c] = 0
                total += len(removable)
            else:
                break
        return total


if __name__ == "__main__":
    Day04().run()
