from math import log
from typing import Optional
from typing import Literal
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from vnstock.explorer.vci.trading import Trading
from vnstock import Quote
from fastmcp import FastMCP, Context
from fastmcp.server.middleware.logging import LoggingMiddleware
from fastmcp.server.middleware.error_handling import (
    ErrorHandlingMiddleware, 
    RetryMiddleware
)
from fastmcp.server.middleware.timing import (
    TimingMiddleware, 
    DetailedTimingMiddleware
)
import asyncio


mcp = FastMCP("Trading MCP Server")

# Comprehensive error logging and transformation
mcp.add_middleware(ErrorHandlingMiddleware(
    include_traceback=True,
    transform_errors=True
))
# Automatic retry with exponential backoff
mcp.add_middleware(RetryMiddleware(
    max_retries=3,
    retry_exceptions=(ConnectionError, TimeoutError)
))
mcp.add_middleware(TimingMiddleware())
mcp.add_middleware(LoggingMiddleware(
    include_payloads=True,
    max_payload_length=1000
))


@mcp.tool
async def get_price_board(symbols: list[str], 
                    ctx: Context,
                    output_format: Literal['json', 'dataframe'] = 'json'):
    """
    Get price board from stock market
    Args:
        symbols: list[str] (list of symbols to get price board)
        output_format: Literal['json', 'dataframe'] = 'json'
    Returns:
        pd.DataFrame
    """
    await ctx.debug("Starting get price_board tool")
    await ctx.info(f"Analyzing {len(symbols)} symbols")

    try:
        trading = Trading()
        df = trading.price_board(symbols_list=symbols)
        if output_format == 'json':
            return df.to_json(orient='records', force_ascii=False)
        else:
            return df
    except Exception as e:
        await ctx.error(f"Analysis failed: {str(e)}")
        raise

    
@mcp.tool
async def get_quote_history_price(symbol: str, 
                            start_date: str, 
                            end_date: str = None, 
                            interval: Literal['1m', '5m', '15m', '30m', '1H', '1D', '1W', '1M'] = '1D', 
                            output_format: Literal['json', 'dataframe'] = 'json',
                            ctx: Context = None):  
    """
    Get quote price history of a symbol from stock market
    Args:
        symbol: str (symbol to get history price)
        start_date: str (format: YYYY-MM-DD)
        end_date: str = None (end date to get history price. None means today)
        interval: Literal['1m', '5m', '15m', '30m', '1H', '1D', '1W', '1M'] = '1D' (interval to get history price)
        output_format: Literal['json', 'dataframe'] = 'json'
    Returns:
        pd.DataFrame
    """
    await ctx.debug("Starting get history price tool")
    await ctx.info(f"Analyzing {symbol} symbols from {start_date} to {end_date}")

    try:
        quote = Quote(symbol=symbol, source='VCI')
        df = quote.history(start=start_date, end=end_date, interval=interval)
        if output_format == 'json':
            return df.to_json(orient='records', force_ascii=False)
        else:
            return df    
    except Exception as e:
        await ctx.error(f"Analysis failed: {str(e)}")
        raise

@mcp.custom_route("/health", methods=["GET"])
def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

def create_mcp_server() -> FastMCP:
    """
    Create and configure the MCP server with all middleware and tools
    Returns:
        FastMCP: Configured MCP server instance
    """
    return mcp


def main(argv: list[str] | None = None):
    """
    Main entry point for the Trading MCP Server.

    Supports the same transport CLI arguments as the top-level `main.py`.
    When invoked as an installed entry point (`src.vnstock_wraper.server:main`),
    this will parse CLI args and run the MCP server accordingly.
    """
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Trading MCP Server')
    parser.add_argument(
        '--transport',
        type=str,
        choices=['stdio', 'sse', 'http', 'streamablehttp'],
        default='http',
        help='Transport mode for the server'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Port number for http/sse modes'
    )
    parser.add_argument(
        '--log-level',
        type=str,
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO',
        help='Logging level'
    )

    args = parser.parse_args(argv if argv is not None else None)

    server = create_mcp_server()
    # Use the async runner provided by FastMCP if available
    try:
        asyncio.run(server.run_async(
            transport=args.transport,
            port=args.port,
            log_level=args.log_level
        ))
    except AttributeError:
        # Fallback if run_async isn't available on the FastMCP instance
        server.run()


if __name__ == "__main__":
    main()

