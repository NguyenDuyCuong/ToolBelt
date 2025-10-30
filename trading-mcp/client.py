import asyncio
from fastmcp import Client, FastMCP
from fastmcp.client.transports import StdioTransport
from fastmcp.client.transports import StreamableHttpTransport

server = FastMCP("server.py:main")
# Basic connection
transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcp")
client = Client(transport)


async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        print(tools)
        
        # Execute operations
        result = await client.call_tool("get_quote_history_price", {"symbol": "CII",
                                                                    "start_date": "2025-10-01", 
                                                                    "end_date": "2025-10-30"})
        print(result)

asyncio.run(main())