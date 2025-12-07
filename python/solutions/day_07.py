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

    def iterate(self, r: int, split: bool) -> int:
        """Iterate either splitting or moving down. Return split count"""
        splits = 0
        for c, col in enumerate(self.grid[r]):
            if not split and col in {"S", "|"} and self.grid[r + 1][c] == ".":
                self.grid[r + 1][c] = "|"
            if split and col == "^" and self.grid[r - 1][c] == "|":
                splits += 1
                if c - 1 >= 0 and self.grid[r][c - 1] == ".":
                    self.grid[r][c - 1] = "|"
                if c + 1 < self.cols and self.grid[r][c + 1] == ".":
                    self.grid[r][c + 1] = "|"
        return splits

    def debug(self) -> None:
        for row in self.grid:
            print("".join(row))

    def part_one(self) -> int:
        """Number of splits"""
        splits = 0
        for r in range(self.rows - 1):
            splits += self.iterate(r, True)
            self.iterate(r, False)
        #     self.debug()
        #     print(splits)
        # self.debug()
        return splits

    @cache
    def timelines(self, r: int, c: int) -> int:
        """How many possible timelines from this cell"""
        cell = self.grid[r][c]

        if cell in {"|", "S"}:
            if r < self.rows - 1:
                return self.timelines(r + 1, c)
            return 0

        if cell == "^":
            left_ok = c > 0 and self.grid[r][c - 1] == "|"
            right_ok = c < self.cols - 1 and self.grid[r][c + 1] == "|"

            if left_ok and right_ok:
                return 1 + self.timelines(r, c - 1) + self.timelines(r, c + 1)
            if left_ok:
                return self.timelines(r, c - 1)
            if right_ok:
                return self.timelines(r, c + 1)

        return 0

    def part_two(self) -> int:
        """Number of timelines"""
        self.part_one()
        start = self.grid[0].index("S")
        # self.debug()
        return 1 + self.timelines(0, start)


if __name__ == "__main__":
    Day07().run()
