const parse = (input: string): number[][] => {
  return input.split("\n").map((row) => row.split("").map(Number));
};

/**
 * Get maximum subarray of the given length with preserved order
 */
const maximumSubarray = (arr: number[], length: number): number => {
  const subArray: number[] = [];
  let remaining = arr;
  for (let i = 0; i < length; i++) {
    const best = Math.max(
      ...remaining.slice(0, remaining.length + i + 1 - length),
    );
    const bestIndex = remaining.indexOf(best);
    subArray.push(best);
    remaining = remaining.slice(bestIndex + 1);
  }
  return parseInt(subArray.join(""));
};

export const part1 = (input: string): number => {
  return parse(input)
    .map((arr) => maximumSubarray(arr, 2))
    .reduce((a, b) => a + b);
};

export const part2 = (input: string): number => {
  return parse(input)
    .map((arr) => maximumSubarray(arr, 12))
    .reduce((a, b) => a + b);
};
