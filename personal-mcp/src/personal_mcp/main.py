"""
Main entry point for the Personal MCP server.
"""

import asyncio
from personal_mcp.server import mcp


async def main():
    """
    Start the Personal MCP server asynchronously.
    """
    await mcp.run_async(transport="http", port=8000)

if __name__ == "__main__":
    asyncio.run(main())
