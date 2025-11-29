from datetime import datetime
from pathlib import Path

import typer
from aocd import get_data, get_puzzle

app = typer.Typer(
    help="Generate Advent of Code solution files",
    context_settings={"help_option_names": ["-h", "--help"]},
)

TODAY = datetime.now().day
ROOT_DIR = Path(__file__).parent.parent.parent
SOLUTION_DIR = ROOT_DIR / "python" / "solutions"
DATA_DIR = ROOT_DIR / "data"

SOLUTION_TEMPLATE = '''from models.aoc_solution import AOCSolution


class Day{day_padded}(AOCSolution):
    EXPECTED = {{
        "part_one": {{"sample": {answer_a}, "data": None}},
        "part_two": {{"sample": {answer_b}, "data": None}},
    }}

    @property
    def parsed_data(self):
        """Parse and return the input data."""
        return self.data.splitlines()

    def part_one(self) -> int:
        """Solve part one."""
        pass

    def part_two(self) -> int:
        """Solve part two."""
        pass


if __name__ == "__main__":
    Day{day_padded}().run()
'''


def create_solution_file(day: int, answer_a: str | None, answer_b: str | None) -> None:
    """Create the solution for the day."""
    day_padded = f"{day:02d}"
    solution_file_path = SOLUTION_DIR / f"day_{day_padded}.py"

    if solution_file_path.exists():
        typer.echo(f"Solution file already exists: {solution_file_path}")
        return

    solution_file_path.write_text(
        SOLUTION_TEMPLATE.format(
            day_padded=day_padded, answer_a=answer_a, answer_b=answer_b
        ),
        encoding="utf-8",
    )
    typer.echo(f"Created solution file: {solution_file_path}")


def fetch_puzzle_data(day: int, year: int) -> tuple[str | None, str | None]:
    """Fetch and save the puzzle input and sample data. Returns (answer_a, answer_b)."""
    data_dir = DATA_DIR / f"day_{day:02d}"
    data_dir.mkdir(parents=True, exist_ok=True)

    data = get_data(day=day, year=year)
    dataset_file = data_dir / "data.txt"
    dataset_file.write_text(data, encoding="utf-8")
    typer.echo(f"Fetched puzzle data: {dataset_file}")

    puzzle = get_puzzle(day=day, year=year)
    examples = puzzle.examples

    if not examples:
        typer.echo("No sample data found")
        return None, None

    example = examples[0]
    sample_file = data_dir / "sample.txt"
    sample_file.write_text(example.input_data, encoding="utf-8")
    typer.echo(f"Fetched sample data: {sample_file}")

    return example.answer_a, example.answer_b


@app.command()
def generate(
    day: int = typer.Option(default=TODAY, help="Day of puzzle"),
    year: int = typer.Option(default=2025, help="Year of puzzle"),
) -> None:
    """Generate solution file and fetch data for a given day."""
    answer_a, answer_b = fetch_puzzle_data(day, year)
    create_solution_file(day, answer_a, answer_b)


if __name__ == "__main__":
    app()
