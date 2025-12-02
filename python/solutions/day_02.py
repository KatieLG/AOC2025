from models.aoc_solution import AOCSolution, Dataset, Part


class Day02(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 1227775554, Dataset.DATA: 38158151648},
        Part.PART_TWO: {Dataset.SAMPLE: 4174379265, Dataset.DATA: 45283684555},
    }

    @staticmethod
    def is_invalid(number: int) -> bool:
        """Check if the number is exactly two repeats of a substring"""
        strnum = str(number)
        length = len(strnum)
        return length % 2 == 0 and strnum[: length // 2] == strnum[length // 2 :]

    @staticmethod
    def is_repeated_substring(number: int) -> bool:
        """Check if the number is formed from repeating substrings"""
        return str(number) in f"{number}{number}"[1:-1] 

    @property
    def parsed_data(self) -> set[int]:
        """Extract all product ids from the provided ranges"""
        product_ids = set()
        for id_range in self.data.split(","):
            first, last = map(int, id_range.split("-"))
            product_ids |= set(range(first, last + 1))
        return product_ids

    def part_one(self) -> int:
        """Solve part one."""
        return sum(pid for pid in self.parsed_data if self.is_invalid(pid))

    def part_two(self) -> int:
        """Solve part two."""
        return sum(pid for pid in self.parsed_data if self.is_repeated_substring(pid))


if __name__ == "__main__":
    Day02().run()
