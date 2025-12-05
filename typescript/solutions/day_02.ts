/**
 * Extract all product ids from the provided ranges
 */
const parse = (input: string): number[] => {
  const productIds = new Set<number>();
  input.split(",").forEach((row) => {
    const [first, last] = row.split("-").map(Number);
    for (let i = first; i <= last; i++) productIds.add(i);
  });
  return Array.from(productIds);
};

/**
 * Check if number is two repeats of another number
 */
const invalid = (num: number): boolean => {
  const strnum = num.toString();
  const length = strnum.length;
  return (
    length % 2 === 0 && strnum.slice(length / 2) === strnum.slice(0, length / 2)
  );
};

const repeatedSubstring = (num: number): boolean => {
  const strnum = num.toString();
  return `${num}${num}`.substring(1, strnum.length * 2 - 1).includes(strnum);
};

export const part1 = (input: string): number => {
  return parse(input)
    .filter(invalid)
    .reduce((a, b) => a + b);
};

export const part2 = (input: string): number => {
  return parse(input)
    .filter(repeatedSubstring)
    .reduce((a, b) => a + b);
};
