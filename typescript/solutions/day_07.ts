import { memoizeDecorator } from "memoize";

class Grid {
  grid: string[][];
  splits: Set<string> = new Set();
  startCol: number;

  constructor(input: string) {
    this.grid = input.split("\n").map((row) => row.split(""));
    this.startCol = this.grid[0].indexOf("S");
  }
  @memoizeDecorator({ cacheKey: (args) => args.join(",") })
  timelines(r: number, c: number): number {
    const cell = this.grid[r][c];
    if (cell == "^") {
      this.splits.add(`${r},${c}`);
      return 1 + this.timelines(r, c - 1) + this.timelines(r, c + 1);
    } else if (r < this.grid.length - 1) {
      return this.timelines(r + 1, c);
    }
    return 0;
  }
}

export const part1 = (input: string): number => {
  const grid = new Grid(input);
  grid.timelines(0, grid.startCol);
  return grid.splits.size;
};

export const part2 = (input: string): number => {
  const grid = new Grid(input);
  return 1 + grid.timelines(0, grid.startCol);
};
