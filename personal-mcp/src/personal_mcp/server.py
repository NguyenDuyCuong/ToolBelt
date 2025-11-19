"""Server setup for the Personal MCP application."""

from fastmcp import FastMCP
from starlette.responses import PlainTextResponse

from personal_mcp.tools import register_tools
from personal_mcp.prompts import register_prompts
from personal_mcp.middwares import register_middwares


# Create server with a descriptive name
mcp = FastMCP("Personal MCP Server")

# Register middlewares
register_middwares(mcp)
# Register all tools and prompts (now from modular registries)
register_tools(mcp)
register_prompts(mcp)

@mcp.custom_route("/health", methods=["GET"])
async def health_check() -> PlainTextResponse:
    """Health check endpoint."""
    return PlainTextResponse("OK")
