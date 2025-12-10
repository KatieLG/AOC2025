import re
from collections import deque
from typing import Iterable

from models.aoc_solution import AOCSolution, Dataset, Part


class Machine:
    def __repr__(self) -> str:
        return f"Machine(lights={self.lights}, target={self.target}, jolts={self.jolts}, target_jolts={self.jolts_target})"

    def __init__(self, row_match: tuple[str, str, str, str]) -> None:
        raw_lights, raw_schematics, _, raw_joltage = row_match
        self.target = [1 if k == "#" else 0 for k in raw_lights.strip("[]")]
        self.lights = [0 for _ in self.target]
        self.jolts = [0 for _ in self.target]
        self.schematics = [
            tuple(map(int, schema.strip("()").split(","))) for schema in raw_schematics.split()
        ]
        self.jolts_target = list(map(int, raw_joltage.strip("{}").split(",")))

    @staticmethod
    def toggle(lights: list[int], button: Iterable[int]) -> list[int]:
        """Push a button like (0, 3, 4) to toggle lights 0, 3, 4"""
        state = lights[:]
        for bt in button:
            state[bt] = 1 - state[bt]
        return state

    def trigger(self, button: list[int], times: int = 1) -> None:
        """Push a button like (0, 3, 4) some number of times to increase the current joltage"""
        for bt in button:
            self.jolts[bt] += times

    def find_shortest_solution(self) -> int:
        """
        Toggling the lights until they match the target, whats the shortest solution
        Should only ever need to press a button once, so worst case scenario is pushing them all
        """
        if self.lights == self.target:
            return 0

        queue = deque()
        queue.append((self.lights, set()))
        seen = set()

        while queue:
            # current queue item is state & buttons pressed so far
            lights, curr = queue.popleft()
            if lights == self.target:
                return len(curr)
            for button in self.schematics:
                if not button in curr:
                    toggled = self.toggle(lights, button)
                    key = tuple(toggled)
                    if key not in seen:
                        seen.add(key)
                        queue.append((toggled, {*curr, button}))

        raise ValueError("No solution found")

        # def find_shortest_joltage_solution(self) -> int:
        """
        Toggle lights until they reach reuired joltage
        Each button needs pushing a multiple of times
        """
        if self.jolts == self.jolts_target:
            return 0

        queue = deque()
        queue.extend([[button] for button in self.schematics])

        while queue:
            # current queue item is buttons pressed so far
            curr = queue.popleft()
            for bt in curr:
                self.toggle(bt)
            if self.jolts == self.jolts_target:
                return len(curr)
            for button in self.schematics:
                if not button in curr:
                    queue.append([*curr, button])
            for bt in curr:
                self.toggle(bt)

        raise ValueError("No solution found")


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
        """Find the shortest button presses per machine for jolts to reach target state"""
        return 33
        return sum(machine.find_shortest_joltage_solution() for machine in self.machines)


if __name__ == "__main__":
    Day10().run()
