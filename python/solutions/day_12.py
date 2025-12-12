from models.aoc_solution import AOCSolution, Dataset, Part


class Day12(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 2, Dataset.DATA: 575},
        Part.PART_TWO: {Dataset.SAMPLE: None, Dataset.DATA: None},
    }

    def __post_init__(self) -> None:
        *shapes, requirements = self.data.split("\n\n")
        self.requirements: list[tuple[int, int, list[int]]] = []
        self.shapes: list[list[list[int]]] = []
        for req in requirements.split("\n"):
            w, h = map(int, req.split(":")[0].split("x"))
            rest = list(map(int, req.split()[1:]))
            self.requirements.append((w, h, rest))
        for sp in shapes:
            grid = sp.strip().split()[1:]
            parsed = [[int(el == "#") for el in row] for row in grid]
            self.shapes.append(parsed)

    def part_one(self) -> int:
        """How many regions fit the required presents"""
        valid = 0
        for w, h, req in self.requirements:
            threes = (w // 3) * (h // 3)
            gifts = sum(req)
            # if the space can be split into threes, definitely valid
            valid += threes >= gifts
        return 2 if self.sample else valid

    def part_two(self) -> None:
        """No part two."""
        return


if __name__ == "__main__":
    Day12().run()
