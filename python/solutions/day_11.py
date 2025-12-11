from functools import cache

from models.aoc_solution import AOCSolution, Dataset, Part


class Day11(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 5, Dataset.DATA: 470},
        Part.PART_TWO: {Dataset.SAMPLE: 0, Dataset.DATA: 384151614084875},
    }

    def __post_init__(self) -> None:
        self.mapping = {row[:3]: row[5:].split() for row in self.data.splitlines()}
        self.find_paths.cache_clear()

    @cache
    def find_paths(self, start: str, end: str) -> int:
        if start == end:
            return 1
        if start not in self.mapping:
            return 0
        nbrs = self.mapping[start]
        return sum(self.find_paths(n, end) for n in nbrs)

    def part_one(self) -> int:
        """Find all paths from `you` to `out`"""
        return self.find_paths("you", "out")

    def part_two(self) -> int:
        """Find all paths from `svr` to `out` passing through `fft` AND `dac`"""
        fft_dac = (
            self.find_paths("svr", "fft")
            * self.find_paths("fft", "dac")
            * self.find_paths("dac", "out")
        )
        dac_fft = (
            self.find_paths("svr", "dac")
            * self.find_paths("dac", "fft")
            * self.find_paths("fft", "out")
        )
        return fft_dac + dac_fft


if __name__ == "__main__":
    Day11().run()
