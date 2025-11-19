"""
Register custom tools for the personal MCP server.
"""

from datetime import datetime, timedelta
from fastmcp import Context
from vnstock import Quote
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

    @mcp.tool
    async def quote_history(
        symbol: str,
        start: str | None = None,
        end: str | None = None,
        interval: str = "1D",
        ctx: Context | None = None,
    ) -> str:
        """
        Retrieves historical OHLC (Open, High, Low, Close) data for a stock symbol.

        Args:
            symbol: Stock symbol (e.g., 'VNM', 'FPT', 'VCI'). Required.
            start: Start date in format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
                   If None, defaults to 30 days ago.
            end: End date in format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
                 If None, defaults to today.
            interval: Data interval. Options: '1m', '5m', '15m', '30m', '1H', '1D' (default), '1W', '1M'.

        Returns:
            A string containing the historical price data formatted as a table or error message.
        """
        if ctx:
            await ctx.log(
                f"Fetching quote history for {symbol} from {start or 'auto'} to {end or 'auto'} "
                f"with interval {interval}"
            )

        try:
            # Validate symbol
            if not symbol or len(symbol) < 3 or len(symbol) > 12:
                return "Error: Symbol must be between 3 and 12 characters long."

            # Set default dates if not provided
            if end is None:
                end = datetime.now().strftime("%Y-%m-%d")
            if start is None:
                start = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

            # Create Quote instance and fetch history
            quote = Quote(symbol=symbol)
            result = quote.history(symbol=symbol, start=start, end=end, interval=interval)

            if result is None or result.empty:
                return f"No data available for {symbol} in the specified date range."

            # Format the result as a readable string
            result_str = result.to_string(index=False)
            return f"Quote History for {symbol} ({start} to {end}, interval: {interval}):\n{result_str}"

        except ValueError as ve:
            return f"Error: {str(ve)}"
        except OSError as ose:
            return f"Connection error: Unable to reach stock data API. {str(ose)}"
        except RuntimeError as re:
            return f"Error fetching data: {str(re)}"
