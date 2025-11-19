### Running the application
- **Run:** `uv run python -m personal_mcp.main`
- **Run in development mode:** `uv run fastmcp dev src/personal_mcp/server.py`
- **Run published/cached package:** `uvx --from . personal-mcp`

### Development commands
- **Linting:** `uv run ruff check .`
- **Formatting:** `uv run ruff format .`
- **Testing:** `uv run pytest`