import { memoizeDecorator } from "memoize";

const parse = (input: string): Map<string, string[]> => {
  return new Map(
    input
      .split("\n")
      .map((line) => [line.slice(0, 3), line.slice(5).split(" ")]),
  );
};

class PathFinder {
  map: Map<string, string[]>;

  constructor(map: Map<string, string[]>) {
    this.map = map;
  }
  @memoizeDecorator({ cacheKey: (args) => args.join(",") })
  findPaths(start: string, end: string): number {
    if (start === end) return 1;
    if (!this.map.has(start)) return 0;
    const nbrs = this.map.get(start)!;
    let totalPaths = 0;
    for (const nbr of nbrs) {
      totalPaths += this.findPaths(nbr, end);
    }
    return totalPaths;
  }
}

export const part1 = (input: string): number => {
  const map = parse(input);
  const pathFinder = new PathFinder(map);
  return pathFinder.findPaths("you", "out");
};

export const part2 = (input: string): number => {
  const map = parse(input);
  const pf = new PathFinder(map);
  const fftDac =
    pf.findPaths("svr", "fft") *
    pf.findPaths("fft", "dac") *
    pf.findPaths("dac", "out");
  const dacFft =
    pf.findPaths("svr", "dac") *
    pf.findPaths("dac", "fft") *
    pf.findPaths("fft", "out");
  return fftDac + dacFft;
};
