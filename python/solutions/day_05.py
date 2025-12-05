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
        return sum(any(start <= iid <= end for start, end in self.ranges) for iid in self.ids)

    def part_two(self) -> int:
        """Count all the IDs in the fresh ranges"""
        total = 0
        max_id = 0
        for start, end in sorted(self.ranges):
            if max_id > end:
                continue
            non_overlapping_start = start if max_id < start else max_id + 1
            total += end - non_overlapping_start + 1
            max_id = end
        return total


if __name__ == "__main__":
    Day05().run()
