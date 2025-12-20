type Vec = [number, number];

const parse = (input: string): Vec[] => {
  return input.split("\n").map((row) => row.split(",").map(Number) as Vec);
};

const area = (a: Vec, b: Vec): number => {
  return Math.abs(-~Math.abs(b[0] - a[0]) * -~Math.abs(b[1] - a[1]));
};

const pairCombinations = <T>(items: T[]): [T, T][] => {
  return items.flatMap((a) => items.map((b) => [a, b] as [T, T]));
};

const pairWise = <T>(items: T[]): [T, T][] => {
  return items.map((a, i) => [a, items[i < items.length - 1 ? i + 1 : 0]]);
};

const sortedCoords = (a: Vec, b: Vec, index: number): [number, number] => {
  return a[index] < b[index] ? [a[index], b[index]] : [b[index], a[index]];
};

export const part1 = (input: string): number => {
  const vectors = parse(input);
  const areas = pairCombinations(vectors).map(([a, b]) => area(a, b));
  areas.sort((a, b) => b - a);
  return areas[0];
};

export const part2 = (input: string): number => {
  const vectors = parse(input);
  const areas: number[] = [];
  const pairs = pairWise(vectors);
  const combos = pairCombinations(vectors);
  combos.forEach(([a, b]) => {
    const [x1, x2] = sortedCoords(a, b, 0);
    const [y1, y2] = sortedCoords(a, b, 1);
    const intersects = pairs.some(([p, q]) => {
      const [p1, p2] = sortedCoords(p, q, 0);
      const [q1, q2] = sortedCoords(p, q, 1);
      return p1 < x2 && p2 > x1 && q1 < y2 && q2 > y1;
    });
    if (!intersects) areas.push(area(a, b));
  });
  areas.sort((a, b) => b - a);
  return areas[0];
};
