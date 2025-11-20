"""
Trading related MCP tools (extracted from original `main.py`).
"""

import logging
from typing import Literal

from vnstock.explorer.vci.trading import Trading as VCITrading
from vnstock import Screener
from mcp_instance import mcp


@mcp.tool()
async def price_board(symbols_list: list[str]):
    """
    Truy xuất thông tin bảng giá của các mã chứng khoán tuỳ chọn từ nguồn dữ liệu VCI.
    Retrieve price board by exchange.

    Tham số:
        - symbols_list: Danh sách các mã chứng khoán cần truy xuất dữ liệu.
        Định dạng dữ liệu đầu vào là Python List.
        Bạn có thể nhập 1 hoặc nhiều mã tuỳ ý.
    """
    logging.info("Processing price_board request...")

    trading = VCITrading()
    return trading.price_board(symbols_list=symbols_list)


@mcp.tool()
async def screener_stocks(
    params: dict = {"exchangeName": "HOSE,HNX,UPCOM"}, 
    limit: int = 1700,
    id: str | None = None,
    lang: Literal['vi', 'en'] = 'vi'
):
    """
    Run a stock screen with given filters.

    Tham số:
        - params: thông số lọc, mặc định chọn cả 3 sàn, bạn không cần nhập gì thêm.
        - limit: Số kết quả tối đa trả về.
        - id:        Optional screener ID.
        - lang:         Language code for multi-language fields ('vi' or 'en').
    """
    logging.info("Processing screener_stocks request...")

    return Screener().stock(params=params, limit=limit, id=id, lang=lang)
