from fastmcp import Context
from vnstock.explorer.misc import sjc_gold_price


def register_tools(mcp):
    """
    Register custom tools for the personal MCP server.
    """

    @mcp.tool
    async def get_sjc_gold_price(
        date: str | None = None, ctx: Context | None = None
    ) -> str:
        """
        Retrieves the SJC gold price for a given date.

        Args:
            date: The date to retrieve gold price for (format: YYYY-MM-DD).
                  If None, uses the current date.

        Returns:
            A string containing the SJC gold price data formatted as a table or error message.
        """
        if ctx:
            await ctx.log(f"Fetching SJC gold price for date: {date or 'today'}")

        try:
            result = sjc_gold_price(date=date)

            if result is None or result.empty:
                return "No data available for the specified date."

            # Format the result as a readable string
            result_str = result.to_string(index=False)
            return f"SJC Gold Prices:\n{result_str}"
        except ValueError as ve:
            return f"Error: {str(ve)}"
        except OSError as ose:
            return f"Connection error: Unable to reach SJC API. {str(ose)}"
        except RuntimeError as re:
            return f"Error fetching data: {str(re)}"
