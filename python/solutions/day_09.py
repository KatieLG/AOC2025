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

    @staticmethod
    def area(a: Vec, b: Vec) -> int:
        """Area between two tiles"""
        return abs(-~abs(b[0] - a[0]) * -~abs(b[1] - a[1]))

    @property
    def parsed_data(self) -> list[Vec]:
        """Parse and return the input data."""
        return [(int(a), int(b)) for row in self.data.splitlines() for a, b in [row.split(",")]]

    def lines_intersect(self, a: Vec, b: Vec, p: Vec, q: Vec) -> bool:
        """Do the lines a -> b and p -> q intersect"""
        (x1, y1), (x2, y2) = sorted([a, b])
        (x3, y3), (x4, y4) = sorted([p, q])
        if x3 == x4:
            return x1 < x3 < x2 and min(y3, y4) < max(y1, y2) >= min(y1, y2) < max(y3, y4)
        if x1 == x2:
            return x3 < x1 < x4 and min(y1, y2) < max(y3, y4) >= min(y3, y4) < max(y1, y2)

        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)

        if m1 == m2:
            # parallel
            return False
        # Want point where y = m1x + c1 is equal to y = m2x + c2
        # i.e. x(m2-m1) = c2 - c1
        c1 = y1 - m1 * x1
        c2 = y3 - m2 * x3
        x_intersect = (c2 - c1) / (m1 - m2)
        y_intersect = m1 * x_intersect + c1

        # print(a, b, p, q, m1, m2, x_intersect, y_intersect)
        # only care if the intersection is within the bounding coords
        return (
            x1 < x_intersect < x2
            and (min(y1, y2) < y_intersect < max(y1, y2) or y1 == y2 == y_intersect)
            and (min(y3, y4) < y_intersect < max(y3, y4) or y3 == y_intersect == y4)
        )

    def part_one(self) -> int:
        """Find maximum area between two tiles"""
        areas = [self.area(a, b) for a, b in itertools.combinations(self.parsed_data, 2)]
        return max(areas)

    def part_two(self) -> int:
        """Find maximum area of any rectangle with only red and green tiles"""
        areas: dict[tuple[Vec, Vec], int] = {}
        fix, ax = plt.subplots()
        for a, b in itertools.combinations(self.parsed_data, 2):
            # Check if the other corners lie outside of the perimeter
            for p, q in itertools.pairwise(self.parsed_data + [self.parsed_data[0]]):
                # If the perimeter is crossed when going from one corner to another, abort
                # i.e. do the lines between a,b and p,q cross
                if self.lines_intersect(a, b, p, q):
                    # plt.plot([a[0], b[0]], [a[1], b[1]], color="red")
                    break
            else:
                ax.plot([a[0], b[0]], [a[1], b[1]], color="blue")
                areas[(a, b)] = self.area(a, b)

        for pt in self.parsed_data:
            ax.plot(*pt, marker="o")
        for a, b in itertools.pairwise(self.parsed_data + [self.parsed_data[0]]):
            ax.plot([a[0], b[0]], [a[1], b[1]], color="yellow")

        largest_rect = max(areas.items(), key=lambda x: x[1])
        a, b = largest_rect[0]

        ax.plot(*a, marker="x")
        ax.plot(*b, marker="x")
        ax.add_patch(
            Rectangle(
                (min(a[0], b[0]), min(a[1], b[1])),
                abs(b[0] - a[0]),
                abs(b[1] - a[1]),
                fill=True,
                color="red",
                zorder=10,
                alpha=0.5,
            )
        )
        plt.show()
        print(largest_rect)
        return largest_rect[1]


if __name__ == "__main__":
    Day09().run()
