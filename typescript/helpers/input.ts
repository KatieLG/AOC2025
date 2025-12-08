import { readFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const dataDir = join(__dirname, "../../data");

export const isSample = (): boolean => {
  return process.env.SAMPLE == "true";
};

export const readInput = (day: string): string => {
  return readFileSync(join(dataDir, day, "data.txt"), "utf-8").trim();
};

export const readSample = (day: string): string => {
  return readFileSync(join(dataDir, day, "sample.txt"), "utf-8").trim();
};
