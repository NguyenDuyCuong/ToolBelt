"""
Tests for the Personal MCP server.
"""

import pytest
from datetime import datetime
from inline_snapshot import snapshot
from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport

from personal_mcp.server import mcp


@pytest.fixture
async def main_mcp_client():
    async with Client(mcp) as mcp_client:
        yield mcp_client


@pytest.mark.asyncio
async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
    list_tools = await main_mcp_client.list_tools()
    assert len(list_tools) == snapshot(2)


@pytest.mark.asyncio
async def test_quote_history_ssi_today(main_mcp_client: Client[FastMCPTransport]):
    """
    Test quote_history for SSI stock on a fixed date.

    This test retrieves the historical OHLC data for SSI stock symbol
    for a fixed date (2025-11-19) and verifies the response structure using snapshot testing.
    """
    fixed_date = "2025-11-19"

    # Call the quote_history tool
    result = await main_mcp_client.call_tool(
        "quote_history",
        {
            "symbol": "SSI",
            "start": fixed_date,
            "end": fixed_date,
            "interval": "1D",
        },
    )

    # Verify the response structure
    assert result is not None
    assert hasattr(result, "content")
    assert len(result.content) > 0

    # Extract text content and verify structure
    text_content = result.content[0].text if result.content else ""
    assert "time" in text_content or "open" in text_content or "close" in text_content

    # Snapshot test for the response metadata
    assert snapshot({"is_error": False, "content_type": "text", "has_data": True}) == {
        "is_error": result.is_error,
        "content_type": result.content[0].type if result.content else None,
        "has_data": len(text_content) > 0,
    }


@pytest.mark.asyncio
async def test_get_sjc_gold_price_fixed_date(main_mcp_client: Client[FastMCPTransport]):
    """
    Test get_sjc_gold_price for a fixed date (2025-11-19) and snapshot metadata.

    This ensures the tool returns content (DataFrame string) and stores
    a stable snapshot for CI comparisons.
    """
    fixed_date = "2025-11-19"

    # Call the get_sjc_gold_price tool
    result = await main_mcp_client.call_tool(
        "get_sjc_gold_price",
        {"date": fixed_date},
    )

    # Basic verifications
    assert result is not None
    assert hasattr(result, "content")
    assert len(result.content) > 0

    # Extract text content and check it contains the fixed date or numeric data
    text_content = result.content[0].text if result.content else ""
    assert fixed_date in text_content or any(c.isdigit() for c in text_content)

    # Snapshot test for response metadata
    assert snapshot({"is_error": False, "content_type": "text", "has_data": True}) == {
        "is_error": result.is_error,
        "content_type": result.content[0].type if result.content else None,
        "has_data": len(text_content) > 0,
    }
