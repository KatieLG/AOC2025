day := $(shell date +%d)
maxlogs := 20

lint:
	uv run ruff check
	uv run ty check

format:
	uv run ruff format
	uv run ruff check --fix

test:
	uv run pytest

check: format lint test

run:
	uv run python -m solutions.day_$(day)

sample:
	uv run python -m solutions.day_$(day) --sample

profile:
	uv run python -m cProfile -s tottime solutions/day_$(day).py | head -n $(maxlogs)
