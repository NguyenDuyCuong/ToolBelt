#!/usr/bin/env python
"""Minimal test server to diagnose the connection issue."""

from fastmcp import FastMCP

# Create server
mcp = FastMCP("Personal MCP Server - Test")

# Register a simple test tool
@mcp.tool()
async def test_tool() -> str:
    """Simple test tool."""
    return "Server is working!"

if __name__ == "__main__":
    # Run with stdio transport
    import sys
    mcp.run(transport="stdio", sys_exit=True)
