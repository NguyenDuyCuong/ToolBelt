from fastmcp import Context
from vnstock import stock_quote

def register_tools(mcp):
    """
    Register custom tools for the personal MCP server.
    """
    # Example tool template (uncomment and customize)
    #
    # @mcp.tool()
    # async def example_tool(param1: str, param2: int = 42):
    #     """
    #     Example tool description.
    #     Args:
    #         param1: Description of the first parameter.
    #         param2: Description of the second parameter (default: 42).
    #     Returns:
    #         A result dictionary or string.
    #     """
    #     # Your tool logic here
    #     result = {"message": f"Received {param1} and {param2}"}
    #     return result
    #
    # Add more tools below as needed.

    @mcp.tool
    async def get_vn_stock_price(symbol: str, ctx: Context) -> str:
        """
        Retrieves the latest price of a stock on the Vietnamese market.

        Args:
            symbol: The stock ticker symbol (e.g., "SSI", "VCB").

        Returns:
            A string containing the latest price of the specified stock.
        """
        await ctx.log(f"Fetching latest price for symbol: {symbol}")
        data = stock_quote(symbol)
        price = data['price'][0]
        return f"The latest price for {symbol} is {price} VND."

    @mcp.tool
    async def greet(name: str, ctx: Context) -> str:
        """
        A simple tool to return a greeting.

        Args:
            name: The name to greet.

        Returns:
            A greeting string.
        """
        await ctx.log(f"Greeting {name}")
        return f"Hello, {name}!"
