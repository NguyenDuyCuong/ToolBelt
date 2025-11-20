"""Tools package for personal MCP server."""

from .vnstock_tools import setup_vnstock_tools


def register_tools(mcp):
    """Register all tools with the MCP server."""
    setup_vnstock_tools(mcp)
