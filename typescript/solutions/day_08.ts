import { isSample } from "../helpers/input";

type Vec = [number, number, number];

const parse = (input: string): Vec[] => {
  return input.split("\n").map((row) => row.split(",").map(Number) as Vec);
};

const dist = (a: Vec, b: Vec): number => {
  const [x1, y1, z1] = a;
  const [x2, y2, z2] = b;
  return Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2);
};

const generatePairs = (vectors: Vec[]): [Vec, Vec][] => {
  const combinations = vectors.flatMap((vec1, i) =>
    vectors.slice(i + 1).map((vec2) => [vec1, vec2] as [Vec, Vec]),
  );
  combinations.sort((a, b) => dist(...b) - dist(...a));
  return combinations;
};

class Playground {
  vectors: Vec[];
  circuits: Vec[][];
  pairs: [Vec, Vec][];

  constructor(input: string) {
    this.vectors = parse(input);
    this.circuits = [];
    this.pairs = generatePairs(this.vectors);
  }
  add_pair(): [Vec, Vec] {
    const [a, b] = this.pairs.pop()!;
    const matches = this.circuits.filter(
      (circ) => circ.includes(a) || circ.includes(b),
    );
    if (matches.length == 0) this.circuits.push([a, b]);
    else if (matches.length == 1) {
      if (!matches[0].includes(a)) matches[0].push(a);
      if (!matches[0].includes(b)) matches[0].push(b);
    } else {
      const [m1, m2] = matches;
      const i2 = this.circuits.indexOf(m2);
      this.circuits.splice(i2, 1);
      m1.push(...m2);
    }
    return [a, b];
  }
  get lengths(): number[] {
    const circuitLengths = this.circuits.map((circ) => circ.length);
    circuitLengths.sort((a, b) => b - a);
    return circuitLengths;
  }
  get isConnected(): boolean {
    return (
      !!this.circuits.length && this.circuits[0].length === this.vectors.length
    );
  }
}

export const part1 = (input: string): number => {
  const playground = new Playground(input);
  const count = isSample() ? 10 : 1000;
  for (let i = 0; i < count; i++) playground.add_pair();
  return playground.lengths.slice(0, 3).reduce((a, b) => a * b);
};

export const part2 = (input: string): number => {
  const playground = new Playground(input);
  let [a, b] = playground.add_pair();
  while (!playground.isConnected) [a, b] = playground.add_pair();
  return a[0] * b[0];
};
