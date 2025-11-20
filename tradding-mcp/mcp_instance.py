"""
MCP instance provider for the project.

Expose a single `mcp` object so tool modules can register with it.
"""
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("tradding-mcp")
