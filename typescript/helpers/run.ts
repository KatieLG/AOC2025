import { readInput, readSample } from "./input";

const useSample = process.env.SAMPLE === "true";
const dayArg = process.argv[2];
const day = dayArg ?? new Date().getDate().toString();

const dayPadded = day.padStart(2, "0");
const input = useSample
  ? readSample(`day_${dayPadded}`)
  : readInput(`day_${dayPadded}`);

const solution = await import(`../solutions/day_${dayPadded}.ts`);

console.log(`Day ${dayPadded}${useSample ? " (sample)" : ""}`);
console.log(`Part 1: ${solution.part1(input)}`);
console.log(`Part 2: ${solution.part2(input)}`);
