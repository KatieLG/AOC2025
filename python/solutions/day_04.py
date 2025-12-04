from models.aoc_solution import AOCSolution, Dataset, Part


class Day04(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 13, Dataset.DATA: 1437},
        Part.PART_TWO: {Dataset.SAMPLE: 43, Dataset.DATA: 8765},
    }

    def __post_init__(self) -> None:
        self.grid = [[int(x == "@") for x in row] for row in self.data.splitlines()]
        self.height = len(self.grid)
        self.width = len(self.grid[-1])

    def count_nbr_rolls(self, r: int, c: int) -> int:
        total = 0
        nbrs = [(r + i, c + j) for i in range(-1, 2) for j in range(-1, 2) if not i == j == 0]
        for y, x in nbrs:
            if y in range(self.height) and x in range(self.width):
                total += self.grid[y][x]
        return total

    def removable(self) -> list[tuple[int, int]]:
        return [
            (r, c)
            for r in range(self.height)
            for c in range(self.width)
            if self.grid[r][c] and self.count_nbr_rolls(r, c) < 4
        ]

    def part_one(self) -> int:
        """Count removable rolls"""
        return len(self.removable())

    def part_two(self) -> int:
        """Keep removing removable rolls until its no longer possible and count total removed"""
        total = 0
        while removable := self.removable():
            for r, c in removable:
                self.grid[r][c] = 0
            total += len(removable)
        return total


if __name__ == "__main__":
    Day04().run()
