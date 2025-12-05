from models.aoc_solution import AOCSolution, Dataset, Part


class Day05(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 3, Dataset.DATA: 782},
        Part.PART_TWO: {Dataset.SAMPLE: 14, Dataset.DATA: 353863745078671},
    }

    def __post_init__(self) -> None:
        ranges, ids = self.data.split("\n\n")
        self.ranges = [
            (int(start), int(end))
            for start, end in (line.split("-") for line in ranges.splitlines())
        ]
        self.ids = [int(line.strip()) for line in ids.splitlines()]

    def part_one(self) -> int:
        """Count all the ingredient IDs that fall into the fresh ranges"""
        fresh = 0
        for iid in self.ids:
            if any((start <= iid <= end) for start, end in self.ranges):
                fresh += 1
        return fresh

    def part_two(self) -> int:
        """Count all the IDs in the fresh ranges"""
        total = 0
        max_covered = -1
        sorted_ranges = sorted(self.ranges, key=lambda r: r[0])
        for start, end in sorted_ranges:
            if max_covered < start:
                max_covered = end
                total += end - start + 1
            elif end > max_covered:
                total += end - max_covered
                max_covered = end
        return total


if __name__ == "__main__":
    Day05().run()
