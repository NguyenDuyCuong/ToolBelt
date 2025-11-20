"""Entrypoint to run the FastMCP server.

This file now only imports the tool modules so they register with the shared
`mcp` instance and then starts the SSE server.
"""

import asyncio
import logging

# Import modules so their `@mcp.tool()` functions register on import.
import company_tools  # noqa: F401
import listing_tools  # noqa: F401
import quote_tools  # noqa: F401

from mcp_instance import mcp


async def main():
    """Run the FastMCP server with SSE support."""
    await mcp.run_sse_async()


if __name__ == "__main__":
    asyncio.run(main())
