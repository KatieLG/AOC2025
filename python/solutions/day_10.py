import re
from collections import deque

from models.aoc_solution import AOCSolution, Dataset, Part


class Machine:

    def __init__(self, row_match: tuple[str, str, str, str]) -> None:
        raw_lights, raw_schematics, _, raw_joltage = row_match
        self.target = int(raw_lights.strip("[],").replace(".", "0").replace("#", "1")[::-1], 2)
        self.lights = 0
        self.schematics = [self.parse_raw_schematic(schema) for schema in raw_schematics.split()]
        self.width = len(bin(max(self.schematics))) - 2
        self.joltage = list(map(int, raw_joltage.strip("{}").split(",")))

    def __repr__(self) -> str:
        w = self.width
        pretty_schematics = [f"{k:0{w}b}" for k in self.schematics]
        return f"Machine(lights={self.lights:0{w}b}, target={self.target:0{w}b}, schematics={pretty_schematics}, joltage={self.joltage})"

    @staticmethod
    def parse_raw_schematic(schematic: str) -> int:
        """Parse (0, 3, 4) into a binary toggle number"""
        mask = 0
        for number in map(int, schematic.strip("()").split(",")):
            mask |= 1 << number
        return mask

    def find_shortest_solution(self) -> int:
        """
        Toggling the lights until they match the target, whats the shortest solution
        Should only ever need to press a button once, so worst case scenario is pushing them all
        """
        if self.lights == self.target:
            return 0

        queue = deque()
        queue.extend([[button] for button in self.schematics])

        while queue:
            # current queue item is buttons pressed so far
            curr = queue.popleft()
            for bt in curr:
                self.lights ^= bt
            if self.lights == self.target:
                return len(curr)
            for button in self.schematics:
                if not button in curr:
                    queue.append([*curr, button])
            for bt in curr:
                self.lights ^= bt

        raise ValueError("No solution to light toggles")


class Day10(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 7, Dataset.DATA: 514},
        Part.PART_TWO: {Dataset.SAMPLE: 33, Dataset.DATA: None},
    }

    def __post_init__(self) -> None:
        self.machines: list[Machine] = []
        for match in re.findall(r"(\[[\.#]*\])((\s*\([\d,]*\))*)\s*({[\d,]*})", self.data):
            self.machines.append(Machine(match))

    def part_one(self) -> int:
        """Find the shortest button presses per machine for lights to reach target state"""
        return sum(machine.find_shortest_solution() for machine in self.machines)

    def part_two(self) -> int:
        """Solve part two."""
        pass


if __name__ == "__main__":
    Day10().run()
