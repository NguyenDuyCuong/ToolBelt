# GitHub Copilot Instructions for personal-mcp

## Project Overview

**personal-mcp** is a Python-based Model Context Protocol (MCP) server built with FastMCP that provides AI agents with tools to access Vietnamese stock market data. The server exposes tools through the MCP protocol and can be deployed locally or integrated with Claude/other AI platforms.

- **Technology Stack**: FastMCP, Pydantic, vnstock, Python 3.13+
- **Package Manager**: `uv` (fast, modern Python package manager)
- **Entry Points**: `uv run python -m personal_mcp.main` (HTTP server) or `fastmcp dev` (development mode)

---

## Architecture & Key Components

### MCP Server Bootstrap Pattern

The project uses a **modular registration pattern**:
- **`server.py`**: Creates FastMCP instance and registers middlewares, tools, and prompts via functions
- **`main.py`**: HTTP server entry point (runs on port 8000 by default)
- **`tools.py`**: Central registry that calls `register_tools(mcp)` to attach tool handlers
- **`prompts.py`**: Prompt template registry (currently unused but reserved for multi-step prompt sequences)
- **`middwares.py`**: Middleware setup (logging, error handling, timing)

Example registration function signature:
```python
def register_tools(mcp):
    @mcp.tool
    async def my_tool(param: str, ctx: Context) -> str:
        await ctx.log(f"Processing {param}")
        return result
```

### Current Tool Implementations

Located in `src/personal_mcp/tools.py`:
- **`get_vn_stock_price(symbol: str)`**: Fetches latest Vietnamese stock price via vnstock
- **`greet(name: str)`**: Simple example tool (for reference)

### Configuration & Middleware Stack

- **`config.py`**: Pydantic Settings loaded from `.env` (extensible for API keys, service URLs)
- **`middwares.py`**: Three middleware layers:
  1. ErrorHandlingMiddleware (traceback + error transformation)
  2. DetailedTimingMiddleware (per-operation timing)
  3. LoggingMiddleware (includes payloads up to 1000 chars)

---

## Development Workflows

### Local Development (Hot Reload)

```bash
uv run fastmcp dev src/personal_mcp/server.py
```
Starts the MCP server with hot-reloading on file changes. Connect via stdio transport in client config.

### Running as HTTP Server

```bash
uv run python -m personal_mcp.main
# Server runs on http://localhost:8000/health
```

### Package Installation & Sync

```bash
uv sync              # Install dependencies + set up .venv
uv run pytest        # Run tests (if added)
```

### Integration in Client (e.g., Claude Desktop)

```json
{
  "mcpServers": {
    "personal-mcp": {
      "command": "uv",
      "args": ["run", "--with", "fastmcp", "fastmcp", "run", "/path/to/server.py"]
    }
  }
}
```

---

## Project-Specific Patterns & Conventions

### Tool Definition Pattern

1. **Always use async functions** for tool handlers
2. **Require `ctx: Context` parameter** for logging/tracing
3. **Return simple types** (str, dict, list) that serialize to JSON
4. **Use docstring as MCP description** (first line = title, rest = detailed help)

```python
@mcp.tool
async def my_feature(ticker: str, ctx: Context) -> str:
    """
    Fetch data for a given ticker.
    
    Args:
        ticker: Stock symbol like "SSI" or "VCB".
    
    Returns:
        Formatted string or JSON-serializable dict.
    """
    await ctx.log(f"Processing {ticker}")
    data = fetch_data(ticker)
    return format_result(data)
```

### vnstock Integration

- Import from `vnstock` (v3.3.0+): `from vnstock import stock_quote, stock_historical_data, listing_companies`
- Always handle possible exceptions from vnstock (missing symbols, rate limits)
- Cache responses in `.env` or memory if implementing repeated queries

### Error Handling Convention

- Let ErrorHandlingMiddleware catch exceptions (no need for try-catch in tools unless custom recovery)
- Include helpful context in error messages via `ctx.log()` before raising

---

## Architectural Future State & Migration

**IMPORTANT**: This project is currently in a **legacy state**. The `GEMINI.md` file defines the target architecture (DDD + SOLID + Functional Programming), but the codebase is still in `src/personal_mcp/` root level.

### Expected Evolution

The vision is to reorganize into:
```
src/personal_mcp/
├── domain/           # Pure domain logic (entities, value objects, services)
├── application/      # Use cases (pipelines, DTOs)
├── interfaces/       # Ports & adapters (MCP tools, providers)
├── infrastructure/   # External integrations (cache, persistence)
└── legacy/           # Deprecated code to be removed
```

### What This Means for AI Agents

- **Current state**: Add new tools to `tools.py` registries directly
- **Do NOT**: Assume the architecture is final—GEMINI.md is the north star
- **When asked to refactor**: Follow GEMINI.md strictly (but this is aspirational, not currently enforced)
- **Dependencies matter**: Avoid introducing unnecessary external libraries; prefer using existing ones (Pydantic, fastmcp, vnstock)

---

## Critical External Dependencies & Notes

| Dependency | Version | Why | Notes |
|---|---|---|---|
| fastmcp | ≥2.13.1 | MCP server framework | Uses async/await, provides decorators like `@mcp.tool` |
| vnstock | ≥3.3.0 | Vietnamese stock data | Only data source currently; may need fallback providers later |
| pydantic | ≥2.12.4 | Data validation | Used in config.py and will be core to domain models |
| pydantic-settings | ≥2.12.0 | Configuration management | Loads .env files safely |

### Known Limitations

1. **Single data source**: Only vnstock is used; no fallback for outages
2. **No persistence**: All queries are live; no caching layer yet
3. **Basic error handling**: Relies on middleware; no custom recovery strategies
4. **No tests**: Test files not yet created; should follow property-based testing (Hypothesis) per GEMINI.md

---

## Common Tasks & How-To

### Adding a New Tool

1. Define the function in `src/personal_mcp/tools.py` with `@mcp.tool` decorator
2. Include full docstring (used by MCP clients as help text)
3. Accept `ctx: Context` parameter for logging
4. Test locally with `uv run fastmcp dev`

### Updating Configuration

1. Add key to `.env` file (NOT committed to git)
2. Reference in `config.py` via Pydantic BaseSettings
3. Access in tools via `from personal_mcp.config import settings`

### Debugging Tool Execution

1. Use `ctx.log(message)` inside tool functions
2. Check middleware logs in server output (LoggingMiddleware includes payloads)
3. Run with `uv run fastmcp dev` for instant feedback

---

## Quick Reference: Commands & Files

| Task | Command | File |
|---|---|---|
| Start dev server | `uv run fastmcp dev src/personal_mcp/server.py` | N/A |
| Start HTTP server | `uv run python -m personal_mcp.main` | `main.py` |
| Add new tool | Edit `tools.py`, then restart | `tools.py` |
| Update config | Edit `.env` and `config.py` | `config.py` |
| View middleware setup | Check `middwares.py` | `middwares.py` |
| Server entry point | Examine `server.py` | `server.py` |

---

## For AI Agents: Important Notes

1. **Always test tools locally** before suggesting integration in `tools.py`
2. **Follow Pydantic v2 patterns** (not v1); use `model_config` over `Config`
3. **Respect async/await**: All tool handlers are async; don't block on I/O
4. **vnstock may change**: Check [vnstock docs](https://vnstock.site/docs/) for breaking changes
5. **This is an MCP server, not a web app**: Don't add REST endpoints; use `@mcp.tool` decorators only (except `/health`)
