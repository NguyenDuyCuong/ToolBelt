"""
Tests for the Personal MCP server.
"""

import pytest
from inline_snapshot import snapshot
from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport

from personal_mcp.server import mcp

@pytest.fixture
async def main_mcp_client():
    async with Client(transport=mcp) as mcp_client:
        yield mcp_client

@pytest.mark.asyncio
async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
    list_tools = await main_mcp_client.list_tools()
    assert len(list_tools) == snapshot(2)
