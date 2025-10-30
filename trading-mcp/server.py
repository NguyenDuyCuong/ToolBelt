from typing import Literal
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from vnstock.explorer.vci.trading import Trading
from vnstock import Quote
from datetime import datetime

mcp = FastMCP("Trading MCP Server")

@mcp.tool
def get_price_board(symbols: list[str], output_format: Literal['json', 'dataframe'] = 'json'):
    """
    Get price board from stock market
    Args:
        symbols: list[str] (list of symbols to get price board)
        output_format: Literal['json', 'dataframe'] = 'json'
    Returns:
        pd.DataFrame
    """
    trading = Trading()
    df = trading.price_board(symbols_list=symbols)
    if output_format == 'json':
        return df.to_json(orient='records', force_ascii=False)
    else:
        return df
    
@mcp.tool
def get_quote_history_price(symbol: str, start_date: str, end_date: str = None, interval: Literal['1m', '5m', '15m', '30m', '1H', '1D', '1W', '1M'] = '1D', output_format: Literal['json', 'dataframe'] = 'json'):  # pyright: ignore[reportUndefinedVariable]  # noqa: F722
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
    quote = Quote(symbol=symbol, source='VCI')
    df = quote.history(start=start_date, end=end_date, interval=interval)
    if output_format == 'json':
        return df.to_json(orient='records', force_ascii=False)
    else:
        return df    

@mcp.custom_route("/health", methods=["GET"])
def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

if __name__ == "__main__":
    mcp.run(transport='http', host='0.0.0.0', port=8000, log_level='DEBUG')