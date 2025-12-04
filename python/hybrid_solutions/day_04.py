from typing import cast

import pyuiua

from models.aoc_solution import AOCSolution, Dataset, Part


class Day04(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 13, Dataset.DATA: 1437},
        Part.PART_TWO: {Dataset.SAMPLE: 43, Dataset.DATA: 8765},
    }

    def __post_init__(self) -> None:
        self.grid: list[list[int]] = pyuiua.eval("⊜(=@@)⊸≠@\\n", self.data)
        self.height = len(self.grid)
        self.width = len(self.grid[-1])

    def removable(self) -> list[list[int]]:
        roll_positions = pyuiua.eval("▽⤚(±⊡)♭₂°⊡", self.grid)
        removable = pyuiua.eval("▽⤚≡⌟(<4⧻(▽⤚⬚0⊡≡⌟+⊂A₂C₂))", roll_positions, self.grid)
        return removable

    def part_one(self) -> int:
        """Count removable rolls"""
        return len(self.removable())

    def part_two(self) -> int:
        """Keep removing removable rolls until its no longer possible and count total removed"""
        total = 0
        while removable := self.removable():
            self.grid: list[list[int]] = pyuiua.eval("⍜⊡×₀", removable, self.grid)
            total += len(removable)
        return total


if __name__ == "__main__":
    Day04().run()
