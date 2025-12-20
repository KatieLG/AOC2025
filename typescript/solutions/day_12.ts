interface Requirement {
  width: number;
  height: number;
  counts: number[];
}

const parse = (input: string): [number[][][], Requirement[]] => {
  const groups = input.split("\n\n");
  const reqText = groups.pop()!;
  const requirements = reqText.split("\n").map((line) => {
    const [w, h] = line.split(":")[0].split("x").map(Number);
    const rest = line.split(" ").slice(1).map(Number);
    return { width: w, height: h, counts: rest };
  });
  const shapes = groups.map((group) =>
    group
      .trim()
      .split("\n")
      .slice(1)
      .map((line) => line.split("").map((char) => (char === "#" ? 1 : 0))),
  );
  return [shapes, requirements];
};

export const part1 = (input: string): number => {
  const [, requirements] = parse(input);
  let valid = 0;
  for (const { width, height, counts } of requirements) {
    const threes = ((width / 3) | 0) * ((height / 3) | 0);
    const gifts = counts.reduce((a, b) => a + b, 0);
    valid += threes >= gifts ? 1 : 0;
  }
  return valid;
};

export const part2 = (_: string): null => {
  return null;
};
