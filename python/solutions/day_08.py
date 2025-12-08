import math
from functools import reduce

from models.aoc_solution import AOCSolution, Dataset, Part

type Vec = tuple[int, int, int]


def vec_dist(a: Vec, b: Vec) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


class Day08(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 40, Dataset.DATA: 32103},
        Part.PART_TWO: {Dataset.SAMPLE: 25272, Dataset.DATA: 8133642976},
    }

    def __post_init__(self) -> None:
        self.used: set[Vec] = set()
        self.vectors = self.parsed_data
        self.pairs = self.generate_pairs()
        self.circuits: list[set[Vec]] = []

    @property
    def parsed_data(self) -> list[Vec]:
        """Return coordinate tuples"""
        return [
            (int(x), int(y), int(z))
            for row in self.data.splitlines()
            for x, y, z in [row.split(",")]
        ]

    def generate_pairs(self) -> list[tuple[Vec, Vec]]:
        dists: dict[tuple[Vec, Vec], float] = {}
        for i, a in enumerate(self.vectors):
            for b in self.vectors[i + 1 :]:
                dist = vec_dist(a, b)
                dists[(a, b)] = dist
        return [key for key, _ in sorted(dists.items(), key=lambda pair: -pair[1])]

    def append_pair(self, a: Vec, b: Vec) -> None:
        """Append vectors to circuit & account for circuit joining"""
        for circ1 in self.circuits:
            if a in circ1:
                for circ2 in self.circuits:
                    if b in circ2:
                        if circ1 == circ2:
                            # Nothing happens
                            return
                        # Circuits join
                        self.circuits.remove(circ2)
                        circ1.update(circ2)
                        return
                # b was not in a circuit so it goes with a
                circ1.add(b)
                return
            if b in circ1:
                for circ2 in self.circuits:
                    if a in circ2:
                        if circ1 == circ2:
                            # Nothing happens
                            return
                        # Circuits join
                        self.circuits.remove(circ2)
                        circ1.update(circ2)
                        return
                # b was not in a circuit so it goes with a
                circ1.add(a)
                return
        # Neither were in a circuit so we get a new circuit
        self.circuits.append({a, b})
        return

    def part_one(self) -> int:
        """Largest 3 circuit sizes multiplied together"""
        counter = 10 if self.sample else 1000
        while counter:
            a, b = self.pairs.pop()
            self.append_pair(a, b)
            counter -= 1

        lengths = [len(circ) for circ in self.circuits]
        best3 = sorted(lengths, reverse=True)[:3]
        return reduce(lambda x, y: x * y, best3)

    def part_two(self) -> int:
        """Multiply x coords of final boxes to join all circuits"""
        while not self.circuits or len(self.circuits[0]) != len(self.vectors):
            a, b = self.pairs.pop()
            self.append_pair(a, b)
        return a[0] * b[0]


if __name__ == "__main__":
    Day08().run()
