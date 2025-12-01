from models.aoc_solution import AOCSolution


class Day01(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 3, "data": 1023},
        "part_two": {"sample": 6, "data": 5899},
    }

    @property
    def parsed_data(self) -> list[tuple[int, int]]:
        """Return tuple of direction and clicks"""
        return [(-1 if row[0] == "L" else 1, int(row[1:])) for row in self.data.splitlines()]

    def part_one(self) -> int:
        """How many times the dial lands on 0 after turning"""
        position = 50
        zeroes = 0
        for direction, clicks in self.parsed_data:
            position += clicks * direction
            position %= 100
            zeroes += position == 0
        return zeroes

    def part_two(self) -> int:
        """How many times the dial passes through 0 during turning"""
        position = 50
        zeroes = 0
        for direction, clicks in self.parsed_data:
            for _ in range(clicks):
                position += direction
                position %= 100
                zeroes += position == 0
        return zeroes


if __name__ == "__main__":
    Day01().run()
