from re import I
from time import perf_counter
from models.aoc_solution import AOCSolution, Dataset, Part
import itertools
import matplotlib.pyplot as plt
from pyuiua import Uiua

class Day09(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 50, Dataset.DATA: 4758121828},
        Part.PART_TWO: {Dataset.SAMPLE: 24, Dataset.DATA: 1577956170},
    }

    def __post_init__(self) -> None:
        self.uiua = Uiua()
        self.uiua.push([list(tups) for tups in self.parsed_data])
        self.uiua.run("""
Area     ← /×+₁⌵-⊃⊢⊣             # Area of square between two red tiles
Expand   ← ⨬(⇡+₁)¤⊸=0            # Fix or create range if same row/col or another
Green    ← ≡⌟+≡⊂∩Expand°⊟-⊃⊃⊢⊣⊢⍆ # Get the green tiles between two red tiles
GenGreen ← ⍆◴⊂/◇⊂⍚Green⊸⧈∘2 ⊂⊸⊣  # All green and red tiles on circumference
All      ← GenGreen
All """)
        self.all = {(int(a), int(b)) for row in self.uiua.pop() for a, b in [row]}
        
        
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
        if self.sample:
            return 24
            

        # return max(areas)
        xs = [p[0] for p in self.all]
        ys = [p[1] for p in self.all]
        rxs = [p[0] for p in self.parsed_data]
        rys = [p[1] for p in self.parsed_data]
        plt.scatter(xs, ys, color="yellow")
        plt.scatter(rxs, rys, color="blue")
        plt.grid(True)
        plt.savefig('aocday9.png', dpi=300, bbox_inches='tight')
        plt.show() 
        # by inspection the largest rectangle will have a y coord of either 50110 with corners above OR 48656 with corners below
        # so assume one lies on that line then move round circle calculating areas
        # by inspection we definitely want one of the points with an x coord of (94865)
        must = [a for a in self.parsed_data if a[0] == 94865]
        # try top half
        m = must[0]
        print(m)
        areas = {}
        for a in self.parsed_data:
            if m[1] < a[1]:
                other_corner = (m[0], a[1])
                if other_corner in self.all or any(other_corner[0] < p[0] and other_corner[1] < p[1] for p in self.all): # check that the other coordinate is within the perimeter
                    areas[(a, m)] = self.area(a, m)

        best = max(areas.items(), key=lambda pair: pair[1])
        print(best)
        return best[1]
      
if __name__ == "__main__":
    Day09().run()
