# Advent of Code 2025

Python solutions for Advent of code 2025

## Setup

1. Setup the session token that AOCD uses:

```bash
echo "session_token" > ~/.config/aocd/token
```

2. Install dependencies:

```bash
uv sync
```

## Puzzle Data

This includes a CLI using the aocd package for automatically generating the solution file for the day and fetching the sample/puzzle data.

```bash
aoc                       # by default generates for today 2025
aoc --day 5 --year 2024   # Provide parameters to generate data for other days
```

This creates:

- `solutions/day_XX.py` - solution template with expected sample answers pre-filled
- `data/day_XX/data.txt` - Puzzle input
- `data/day_XX/sample.txt` - Sample input from the puzzle description

## Dev Commands

| Command                | Description                               |
| ---------------------- | ----------------------------------------- |
| `make run`             | Run today's solution                      |
| `make run day=01`      | Run solution for specified day            |
| `make sample day=01`   | Run solution with sample input            |
| `make profile day=01`  | Profile solution with cProfile            |
| `make format`          | Format code with ruff                     |
| `make lint`            | Lint with ruff and type check with ty     |
| `make test`            | Run unit tests                            |
| `make check`           | Run format, lint, and test                |
