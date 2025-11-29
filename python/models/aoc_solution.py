import sys
from abc import ABC, abstractmethod
from enum import StrEnum
from pathlib import Path
from typing import TypedDict


class Dataset(StrEnum):
    SAMPLE = "sample"
    DATA = "data"


class Part(StrEnum):
    PART_ONE = "part_one"
    PART_TWO = "part_two"


class ExpectedResult(TypedDict):
    sample: str | int | None
    data: str | int | None


class AOCSolution(ABC):
    EXPECTED: dict[Part, ExpectedResult]

    def __init__(self) -> None:
        self.day = int(self.__class__.__name__.replace("Day", ""))
        self.root = Path(__file__).parent.parent.parent
        self.data = ""
        self.sample = False

    def set_data(self, dataset: Dataset) -> None:
        folder = f"data/day_{self.day:02d}"
        filename = "sample" if dataset == Dataset.SAMPLE else "data"
        self.sample = dataset == Dataset.SAMPLE
        self.data = Path(self.root, f"{folder}/{filename}.txt").read_text(
            encoding="utf-8"
        )
        self.__post_init__()

    def __post_init__(self) -> None: ...

    @abstractmethod
    def part_one(self) -> int | str: ...

    @abstractmethod
    def part_two(self) -> int | str: ...

    def _check_result(self, part: Part, result: int | str, dataset: Dataset) -> str:
        expected = self.EXPECTED.get(part, {}).get(dataset)
        if expected is None:
            return ""
        if result == expected:
            return " ✓"
        return f" ✗ (expected {expected})"

    def run(self) -> None:
        iterable = [Dataset.SAMPLE] if "--sample" in sys.argv else Dataset
        for dataset in iterable:
            self.set_data(dataset)
            print(dataset.value.capitalize())
            for part in Part:
                result = getattr(self, part)()
                status = self._check_result(part, result, dataset)
                print(f"{part}: {result}{status}")
