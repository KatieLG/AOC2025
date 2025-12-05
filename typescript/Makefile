day := $(shell date +%d)

lint:
	npm run lint

format: 
	npm run format

test:
	npm test

check: format lint test

run:
	npm run day -- $(day)

sample:
	npm run sample -- $(day)

setup:
	@if [ -f solutions/day_$(day).ts ]; then \
		echo "solutions/day_$(day).ts already exists"; \
	else \
		printf '%s\n' \
			'export const part1 = (input: string) => {' \
			'  return input;' \
			'};' \
			'' \
			'export const part2 = (input: string) => {' \
			'  return input;' \
			'};' > solutions/day_$(day).ts; \
	fi
