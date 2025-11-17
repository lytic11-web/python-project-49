
# Install dependencies
install:
	uv sync

# Run the brain-games application
brain-games:
	uv run brain-games

# Build the package
build:
	uv build

# Install the built package system-wide
package-install:
	uv tool install dist/*.whl

# Run the linter
lint:
	uv run ruff check brain_games
