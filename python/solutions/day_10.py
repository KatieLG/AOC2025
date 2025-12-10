from collections import deque
import re

from models.aoc_solution import AOCSolution, Dataset, Part


class Machine:
    def __repr__(self) -> str:
        return f"Machine(lights={self.lights}, target={self.target}, schematics={self.schematics}, joltage={self.joltage})"

    def __init__(self, row_match: tuple[str, str, str, str]) -> None:
        raw_lights, raw_schematics, _, raw_joltage = row_match
        self.target = [1 if k == "#" else 0 for k in raw_lights.strip("[]")]
        self.lights = [0 for _ in self.target]
        self.schematics = [
            list(map(int, schema.strip("()").split(","))) for schema in raw_schematics.split()
        ]
        self.joltage = list(map(int, raw_joltage.strip("{}").split(",")))

    def toggle(self, button: list[int]) -> None:
        """Push a button like (0, 3, 4) to toggle lights 0, 3, 4"""
        for bt in button:
            self.lights[bt] = 1 - self.lights[bt]

    def find_shortest_solution(self, used: list[list[int]] | None = None) -> int:
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
                self.toggle(bt)
            if self.lights == self.target:
                return len(curr)
            for button in self.schematics:
                if not button in curr:
                    queue.append([*curr, button])
            for bt in curr:
                self.toggle(bt)

        return 0


class Day10(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 7, Dataset.DATA: 514},
        Part.PART_TWO: {Dataset.SAMPLE: None, Dataset.DATA: None},
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
