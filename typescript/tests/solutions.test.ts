import { describe, expect, it } from "vitest";
import { readInput } from "../helpers/input.js";

const expected: Record<string, [number | string, number | string]> = {
  day_01: [1023, 5899],
  day_02: [38158151648, 45283684555],
  day_03: [17316, 171741365473332],
  day_04: [1437, 8765],
  day_05: [782, 353863745078671],
  day_07: [1660, 305999729392659],
  day_08: [32103, 8133642976],
  day_09: [4758121828, 1577956170]
};

for (const [day, [expectedPart1, expectedPart2]] of Object.entries(expected)) {
  describe(day, async () => {
    const solution = await import(`../solutions/${day}.ts`);
    const input = readInput(day);

    it("part1", () => {
      expect(solution.part1(input)).toBe(expectedPart1);
    });

    it("part2", () => {
      expect(solution.part2(input)).toBe(expectedPart2);
    });
  });
}
