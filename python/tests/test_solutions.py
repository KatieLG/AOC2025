from importlib import import_module
from types import ModuleType

import pytest

from models.aoc_solution import AOCSolution, Dataset, Part


def _load_module(name: str) -> ModuleType | None:
    """Don't test modules that don't exist yet"""
    try:
        return import_module(name)
    except ModuleNotFoundError:
        return None


def _load_modules(directory: str) -> list[ModuleType]:
    return [
        module for day in range(1, 13) if (module := _load_module(f"{directory}.day_{day:02d}"))
    ]


@pytest.mark.parametrize("module", _load_modules("solutions"))
@pytest.mark.parametrize("dataset", Dataset)
@pytest.mark.parametrize("part", Part)
def test_solution(module: ModuleType, dataset: Dataset, part: Part) -> None:
    day = module.__name__[-2:]
    solution: AOCSolution = getattr(module, f"Day{day}")()
    solution.set_data(dataset)
    assert getattr(solution, part)() == solution.EXPECTED[part][dataset]


@pytest.mark.parametrize("module", _load_modules("hybrid_solutions"))
@pytest.mark.parametrize("dataset", Dataset)
@pytest.mark.parametrize("part", Part)
def test_hybrid_solution(module: ModuleType, dataset: Dataset, part: Part) -> None:
    day = module.__name__[-2:]
    solution: AOCSolution = getattr(module, f"Day{day}")()
    solution.set_data(dataset)
    assert getattr(solution, part)() == solution.EXPECTED[part][dataset]
