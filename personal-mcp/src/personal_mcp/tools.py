from fastmcp import Context

def register_tools(mcp):
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
    async def greet(name: str, ctx: Context) -> str:
        await ctx.log(f"Greeting {name}")
        return f"Hello, {name}!"
