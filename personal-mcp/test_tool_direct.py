"""
Direct test of quote_history tool without running server.
"""
import asyncio
from datetime import datetime, timedelta
from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport
from personal_mcp.server import mcp


async def test_quote_history():
    """Test quote_history tool directly."""
    async with Client(mcp) as client:
        # Test with SSI
        print("📊 Testing quote_history with SSI...")
        result = await client.call_tool(
            "quote_history",
            {
                "symbol": "SSI",
                "start": "2025-11-01",
                "end": "2025-11-20",
                "interval": "1D",
            },
        )
        
        print(f"✓ Result Type: {type(result)}")
        print(f"✓ Is Error: {result.is_error}")
        print(f"✓ Content Length: {len(result.content)}")
        
        if result.content:
            text = result.content[0].text
            print(f"\n📈 Response (first 500 chars):\n")
            print(text[:500])
            print(f"\n... (total: {len(text)} chars)")
        
        return result


async def test_screener():
    """Test screener_stock tool - one that's available."""
    async with Client(mcp) as client:
        print("\n\n📊 Testing screener_stock tool...")
        result = await client.call_tool(
            "screener_stock",
            {"limit": 5},
        )
        
        print(f"✓ Result Type: {type(result)}")
        print(f"✓ Is Error: {result.is_error}")
        print(f"✓ Content Length: {len(result.content)}")
        
        if result.content:
            text = result.content[0].text
            print(f"\n📊 Response (first 500 chars):\n")
            print(text[:500])
            print(f"\n... (total: {len(text)} chars)")
        
        return result


async def main():
    try:
        await test_quote_history()
        await test_screener()
        print("\n✅ All tests passed!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
