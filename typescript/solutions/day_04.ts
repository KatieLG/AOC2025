/**
 * Create a bit grid from input data
 */
const parse = (input: string): number[][] => {
  return input
    .split("\n")
    .map((row) => row.split("").map((el) => (el === "@" ? 1 : 0)));
};

/**
 * Count the adjacent & diagonal neighbours which are also rolls
 */
const countNbrs = (grid: number[][], row: number, column: number): number => {
  let nbrs = 0;
  for (let x = column - 1; x < column + 2; x++) {
    for (let y = row - 1; y < row + 2; y++) {
      if (x === column && y == row) continue;
      if (
        0 <= x &&
        x < grid[0].length &&
        0 <= y &&
        y < grid.length &&
        !!grid[y][x]
      )
        nbrs += 1;
    }
  }
  return nbrs;
};

/**
 * Find the rolls with <4 Nbrs which can be removed
 */
const removeable = (grid: number[][]): [number, number][] => {
  return grid.flatMap((row, i) => {
    return row
      .map((el, j) => {
        return (
          el === 1 && countNbrs(grid, i, j) < 4 && ([i, j] as [number, number])
        );
      })
      .filter((record) => !!record);
  });
};

export const part1 = (input: string): number => {
  const grid = parse(input);
  return removeable(grid).length;
};

export const part2 = (input: string): number => {
  let total = 0;
  const grid = parse(input);
  while (true) {
    const toRemove = removeable(grid);
    if (!toRemove.length) break;

    for (const [row, column] of toRemove) grid[row][column] = 0;
    total += toRemove.length;
  }
  return total;
};
