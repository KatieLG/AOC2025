const parse = (input: string): [[number, number][], number[]] => {
  const [ranges, ids] = input.split("\n\n");
  const rangeTuples = ranges
    .split("\n")
    .map((line) => line.split("-").map(Number) as [number, number]);
  const idList = ids.split("\n").map(Number);
  return [rangeTuples, idList];
};

const compareRanges = (
  rangeA: [number, number],
  rangeB: [number, number],
): number => {
  return rangeA[0] < rangeB[0] ? -1 : 1;
};

export const part1 = (input: string): number => {
  const [ranges, ids] = parse(input);
  return ids.filter((iid) =>
    ranges.some(([start, end]) => start <= iid && iid <= end),
  ).length;
};

export const part2 = (input: string): number => {
  const [ranges] = parse(input);
  let total = 0;
  let maxId = 0;
  for (const [start, end] of ranges.toSorted(compareRanges)) {
    if (maxId > end) continue;
    const nonOverlappingStart = maxId < start ? start : maxId + 1;
    total += end - nonOverlappingStart + 1;
    maxId = end;
  }
  return total;
};
