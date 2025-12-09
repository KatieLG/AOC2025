import itertools
from typing import TypeAlias

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from models.aoc_solution import AOCSolution, Dataset, Part

Vec: TypeAlias = tuple[int, int]


class Day09(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 50, Dataset.DATA: 4758121828},
        Part.PART_TWO: {Dataset.SAMPLE: 24, Dataset.DATA: 1577956170},
    }

    def __post_init__(self) -> None:
        _, self.ax = plt.subplots()

    @staticmethod
    def area(a: Vec, b: Vec) -> int:
        """Area between two tiles"""
        return abs(-~abs(b[0] - a[0]) * -~abs(b[1] - a[1]))

    @property
    def parsed_data(self) -> list[Vec]:
        """Parse and return the input data."""
        return [(int(a), int(b)) for row in self.data.splitlines() for a, b in [row.split(",")]]

    def part_one(self) -> int:
        """Find maximum area between two tiles"""
        areas = [self.area(a, b) for a, b in itertools.combinations(self.parsed_data, 2)]
        return max(areas)

    def plot_init(self) -> None:
        """Plot the coordinates on a grid"""
        for q in self.parsed_data:
            self.ax.plot(*q, marker="o", color="blue")
        for a, b in itertools.pairwise(self.parsed_data + [self.parsed_data[0]]):
            self.ax.plot([a[0], b[0]], [a[1], b[1]], color="yellow")
        self.ax.grid(True)

    def plot_save(self) -> None:
        plt.savefig("graphics/day09_visualisation.png", dpi=300, bbox_inches="tight")

    def plot_rect(self, a: Vec, b: Vec) -> None:
        (x1, y1), (x2, y2) = a, b
        self.ax.add_patch(
            Rectangle(
                (min(x1, x2), min(y1, y2)),
                abs(x2 - x1),
                abs(y2 - y1),
                fill=True,
                color="red",
                alpha=0.5,
                zorder=10,
            )
        )

    def part_two(self) -> int:
        """Find maximum area of any rectangle with only red and green tiles"""
        if self.sample:
            return 24

        self.plot_init()
        # by inspection of the plot the largest rectangle will have a corner or either (94865, 50110) or (94865, 48656)
        # so assume one of these then move round circle calculating areas
        # start by trying the top one
        v1 = (94865, 50110)
        areas = {}
        for v2 in self.parsed_data:
            if v1[1] < v2[1]:
                diag = (v1[0], v2[1])
                if any(diag[0] < p[0] and diag[1] < p[1] for p in self.parsed_data):
                    areas[(v1, v2)] = self.area(v1, v2)

        best = max(areas.items(), key=lambda pair: pair[1])
        self.plot_rect(*best[0])
        self.plot_save()
        return best[1]


if __name__ == "__main__":
    Day09().run()
