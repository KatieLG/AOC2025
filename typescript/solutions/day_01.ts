const parse = (input: string) => {
  return input
    .split("\n")
    .map((row) => [row[0] === "L" ? -1 : 1, parseInt(row.slice(1))]);
};

export const part1 = (input: string) => {
  let position = 50;
  let zeroes = 0;
  parse(input).map(([direction, clicks]) => {
    position += clicks * direction;
    position %= 100;
    zeroes += position === 0 ? 1 : 0;
  });
  return zeroes;
};

export const part2 = (input: string) => {
  let position = 50;
  let zeroes = 0;
  parse(input).map(([direction, clicks]) => {
    const clicks_to_next_zero = (10000 - direction * position) % 100;
    zeroes += - Math.floor((clicks_to_next_zero - clicks) / 100);
    position += clicks * direction;
    position %= 100;
  });
  return zeroes;
};
