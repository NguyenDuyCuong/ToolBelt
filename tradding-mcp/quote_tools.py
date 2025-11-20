"""
Quote related MCP tools (extracted from original `main.py`).
"""

import logging
from typing import Literal

from vnstock import Quote, Vnstock
from mcp_instance import mcp


@mcp.tool()
async def history(
    symbol: str,
    start: str,
    end: str,
    interval: str = "1d",
    source: Literal["VCI", "TCBS"] = "VCI",
):
    """
    Load historical OHLC data for the symbol. Tải dữ liệu OHLC lịch sử cho mã chứng khoán.
    Retrieve historical quote data.

    Tham số:
        - symbol : str, optional
        Stock symbol. Mã chứng khoán.

        - start : str
        Start time in format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
        Thời gian bắt đầu định dạng YYYY-MM-DD hoặc YYYY-MM-DD HH:MM:SS.

        - end : str
        End time in format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
        Thời gian kết thúc định dạng YYYY-MM-DD hoặc YYYY-MM-DD HH:MM:SS.

        - interval : str, optional
        Data interval (1m, 5m, 15m, 30m, 1H, D, 1W, 1M).
        Khoảng thời gian dữ liệu (1m, 5m, 15m, 30m, 1H, D, 1W, 1M).
    """
    logging.info("Processing history request...")

    quote = Quote(symbol=symbol, source=source)
    return quote.history(start=start, end=end, interval=interval)


@mcp.tool()
async def intraday(
    symbol: str,
    page_size: int = 100,
    page: int = 1,
    source: Literal["VCI", "TCBS"] = "VCI",
):
    """
    Load intraday trade data for the symbol. Tải dữ liệu giao dịch trong ngày cho mã chứng khoán.
    Retrieve intraday quote data.

    Tham số:
        - symbol : str, optional
        Stock symbol. Mã chứng khoán.

        - page_size : int, optional
        Number of records to return. Số lượng bản ghi trả về.

        - page : int, optional
        Page number. Số trang.
    """
    logging.info("Processing intraday request...")

    quote = Quote(symbol=symbol, source=source)
    return quote.intraday(page_size=page_size, page=page)


@mcp.tool()
async def price_depth(
    symbol: str,
    source: Literal["VCI", "TCBS"] = "VCI",
):
    """
    Load price depth (order book) data for the symbol.
    Tải dữ liệu độ sâu giá (sổ lệnh) cho mã chứng khoán.
    Retrieve price depth quote data.

    Tham số:
        - symbol : str, optional
        Stock symbol. Mã chứng khoán.
    """
    logging.info("Processing price_depth request...")

    quote = Quote(symbol=symbol, source=source)
    return quote.price_depth()


@mcp.tool()
async def forex_history(symbol: str, start: str, end: str, interval: str = "1D"):
    """
    Load historical OHLC data for the forex symbol.
    Retrieve historical forex quote data.

    Tham số:
        - symbol: Mã cặp tiền tệ cần tra cứu.
        Hiện tại hàm hỗ trợ truy xuất dữ liệu trực tiếp cho các cặp tiền tệ sau:USDVND, JPYVND, AUDVND, CNYVND, KRWVND, USDJPY, USDEUR, USDCAD, USDCHF, USDCNY, USDKRW, USDSGD, USDHKD, USDTRY, USDINR, USDDKK, USDSEK, USDILS, USDRUB, USDMXN, USDZAR, EURUSD, EURVND, EURJPY, EURGBP, EURCHF, EURCAD, EURAUD, EURNZD, GBPJPY, GBPVND, GBPUSD, GBPAUD, GBPCHF, GBPNZD, GBPCAD, AUDUSD, NZDUSD.
        - start: Ngày kết thúc của truy vấn dữ liệu lịch sử. Định dạng YYYY-mm-dd
        - end: Ngày kết thúc của truy vấn dữ liệu lịch sử. Định dạng YYYY-mm-dd
        - interval (tuỳ chọn): Khung thời gian lấy mẫu dữ liệu. Chỉ hỗ trợ giá trị "1D" để lấy dữ liệu cuối ngày.
    """
    logging.info("Processing forex_history request...")

    fx = Vnstock().fx(symbol=symbol, source="MSN")
    return fx.quote.history(start=start, end=end, interval=interval)


@mcp.tool()
async def crypto_history(symbol: str, start: str, end: str, interval: str = "1D"):
    """
    Load historical OHLC data for the crypto symbol.
    Retrieve historical crypto quote data.

    Tham số:
        - symbol: Mã crypto bạn cần tra cứu. Hiện tại hỗ trợ các mã sau: BTC, ETH, USDT, USDC, BNB, BUSD, XRP, ADA, SOL, DOGE
        - start: Ngày kết thúc của truy vấn dữ liệu lịch sử. Định dạng YYYY-mm-dd
        - end: Ngày kết thúc của truy vấn dữ liệu lịch sử. Định dạng YYYY-mm-dd
        - interval (tuỳ chọn): Khung thời gian lấy mẫu dữ liệu. Chỉ hỗ trợ giá trị "1D" để lấy dữ liệu cuối ngày.
    """
    logging.info("Processing crypto_history request...")

    crypto = Vnstock().crypto(symbol=symbol, source="MSN")
    return crypto.quote.history(start=start, end=end, interval=interval)


@mcp.tool()
async def world_index_history(symbol: str, start: str, end: str, interval: str = "1D"):
    """
    Load historical OHLC data for the world index symbol.
    Retrieve historical world index quote data.

    Tham số:
        - symbol: mã chỉ số bạn cần tra cứu. Sử dụng một trong các mã sau:
            INX: S&P 500 Index
            DJI: Dow Jones Industrial Average
            COMP: Nasdaq Composite Index
            RUT: Russell 2000 Index
            NYA: NYSE Composite Index
            RUI: Russell 1000 Index
            RUA: Russell 3000 Index
            UKX: FTSE 100 Index
            DAX: DAX Index
            PX1: CAC 40 Index
            N225: Nikkei 225 Index
            000001: Shanghai SE Composite Index
            HSI: Hang Seng Index
            SENSEX: S&P BSE Sensex Index
            ME00000000: S&P/BMV IPC
        - start: Ngày kết thúc của truy vấn dữ liệu lịch sử. Định dạng YYYY-mm-dd
        - end: Ngày kết thúc của truy vấn dữ liệu lịch sử. Định dạng YYYY-mm-dd
        - interval (tuỳ chọn): Khung thời gian lấy mẫu dữ liệu. Chỉ hỗ trợ giá trị "1D" để lấy dữ liệu cuối ngày.
    """
    logging.info("Processing world_index_history request...")

    world_index = Vnstock().world_index(symbol=symbol, source="MSN")
    return world_index.quote.history(start=start, end=end, interval=interval)
