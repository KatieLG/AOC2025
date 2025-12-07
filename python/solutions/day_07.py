from functools import cache

from models.aoc_solution import AOCSolution, Dataset, Part


class Day07(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 21, Dataset.DATA: 1660},
        Part.PART_TWO: {Dataset.SAMPLE: 40, Dataset.DATA: 305999729392659},
    }

    def __post_init__(self) -> None:
        self.grid = [list(row) for row in self.data.splitlines()]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.splits: set[tuple[int, int]] = set()
        self.start = self.grid[0].index("S")

    @cache
    def timelines(self, r: int, c: int) -> int:
        """
        How many possible timelines from this cell
        Has a side effect of split counting
        """
        cell = self.grid[r][c]

        if cell in {".", "S"} and r < self.rows - 1:
            return self.timelines(r + 1, c)

        if cell == "^":
            if c > 0 and c < self.cols - 1:
                self.splits.add((r, c))
                return 1 + self.timelines(r, c - 1) + self.timelines(r, c + 1)
            if c > 0:
                return self.timelines(r, c - 1)
            if c < self.cols - 1:
                return self.timelines(r, c + 1)

        return 0

    def part_one(self) -> int:
        """Number of splits"""
        self.timelines(0, self.start)
        return len(self.splits)

    def part_two(self) -> int:
        """Number of timelines from start position"""
        return 1 + self.timelines(0, self.start)


if __name__ == "__main__":
    Day07().run()
