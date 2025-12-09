from re import I
from models.aoc_solution import AOCSolution, Dataset, Part
import itertools

class Day09(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 50, Dataset.DATA: 4758121828},
        Part.PART_TWO: {Dataset.SAMPLE: 24, Dataset.DATA: None},
    }

    @staticmethod
    def area(a: tuple[int, int], b: tuple[int, int]) -> int:
        """Area between two tiles"""
        return abs(-~abs(b[0] - a[0]) * -~abs(b[1] - a[1]))

    @property
    def parsed_data(self) -> list[tuple[int, int]]:
        """Parse and return the input data."""
        return [(int(a), int(b)) for row in self.data.splitlines() for a, b in [row.split(",")]]

    def part_one(self) -> int:
        """Find maximum area between two tiles"""
        areas = [self.area(a, b) for a, b in itertools.combinations(self.parsed_data, 2)]
        return max(areas)

    def part_two(self) -> int:
        """Find maximum area of any rectangle with only red and green tiles"""
        # areas: list[int] = []
        # for a, b in itertools.combinations(self.parsed_data, 2):
        #     # corners
        #     c1 = a[0], b[1]
        #     c2 = b[0], a[1]
            

        # return max(areas)
        return 0


if __name__ == "__main__":
    Day09().run()
