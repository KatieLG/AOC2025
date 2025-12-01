day := $(shell date +%d)

test:
	uiua run tests/test_solutions.ua

run:
	uiua run solutions/day_$(day).ua

setup:
	@if [ -f solutions/day_$(day).ua ]; then \
		echo "solutions/day_$(day).ua already exists"; \
	else \
		printf '%s\n' \
			'~ "../helpers/input.ua" ~ ReadSample' \
			'' \
			'Data ← (' \
			'  ReadSample "day_$(day)"' \
			')' \
			'' \
			'Data' \
			> solutions/day_$(day).ua; \
	fi
