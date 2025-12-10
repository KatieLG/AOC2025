import re
from collections import deque
from typing import Iterable

import numpy as np
import scipy

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

    @staticmethod
    def trigger(jolts: list[int], button: Iterable[int], times: int = 1) -> list[int]:
        """Push a button like (0, 3, 4) some number of times to increase the current joltage"""
        state = jolts[:]
        for bt in button:
            state[bt] += times
        return state

    def find_shortest_solution(self) -> int:
        """
        Toggling the lights until they match the target, whats the shortest solution
        Should only ever need to press a button once, so worst case scenario is pushing them all
        """
        queue = deque()
        queue.append((self.lights, set()))
        seen = set()

        while queue:
            # current queue item is state & buttons pressed so far
            lights, curr = queue.popleft()
            if lights == self.target:
                return len(curr)
            if tuple(lights) in seen:
                continue
            seen.add(tuple(lights))
            for button in self.schematics:
                if button not in curr:
                    toggled = self.toggle(lights, button)
                    queue.append((toggled, {*curr, button}))

        raise ValueError("No solution found")

    def find_shortest_joltage_solution(self) -> int:
        """
        Toggle lights until they reach reuired joltage
        Each button needs pushing a multiple of times
        """
        button_vectors = [self.trigger(self.jolts, button) for button in self.schematics]
        btn_matrix = np.array(button_vectors).T
        sln_vector = np.array(self.jolts_target)
        minimisation_vector = np.ones(btn_matrix.shape[1])  # for minimising coefficients
        bounds = [(0, None)] * btn_matrix.shape[1]  # 0 as lower bound, nothing as upper bound
        integrality = [1] * btn_matrix.shape[1]  # enforce ints for all coefficients
        result = scipy.optimize.linprog(
            minimisation_vector,
            A_eq=btn_matrix,
            b_eq=sln_vector,
            bounds=bounds,
            integrality=integrality,
        )
        return int(sum(result.x))


class Day10(AOCSolution):
    EXPECTED = {
        Part.PART_ONE: {Dataset.SAMPLE: 7, Dataset.DATA: 514},
        Part.PART_TWO: {Dataset.SAMPLE: 33, Dataset.DATA: 21824},
    }

    def __post_init__(self) -> None:
        self.machines: list[Machine] = []
        for match in re.findall(r"(\[[.#]*])((\s*\([\d,]*\))*)\s*({[\d,]*})", self.data):
            self.machines.append(Machine(match))

    def part_one(self) -> int:
        """Find the shortest button presses per machine for lights to reach target state"""
        return sum(machine.find_shortest_solution() for machine in self.machines)

    def part_two(self) -> int:
        """Find the shortest button presses per machine for jolts to reach target state"""
        return sum(machine.find_shortest_joltage_solution() for machine in self.machines)


if __name__ == "__main__":
    Day10().run()
