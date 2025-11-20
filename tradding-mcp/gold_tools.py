"""
Gold tools for market data retrieval.
"""

import logging

from vnstock.explorer.misc.gold_price import * 
from vnstock.explorer.misc.exchange_rate import *
from mcp_instance import mcp


@mcp.tool()
async def get_sjc_gold_price(date: str = None):
    """
    Truy xuất giá vàng SJC hiện tại.
    Retrieve current SJC gold price.
    Args:
    - date (tùy chọn): Ngày tra cứu, mặc định là None để lấy ngày hiện tại. 
    Nhập giá trị tùy chọn, định dạng YYYY-mm-dd, ví dụ 2025-01-15. 
    Dữ liệu có sẵn từ ngày 2/1/2016.
    """
    logging.info("Processing sjc_gold_price request...")

    return sjc_gold_price(date=date)


@mcp.tool()
async def get_btmc_goldprice():
    """
    Parse dữ liệu giá vàng từ API JSON Bảo Tín Minh Châu.
    """
    logging.info("Processing btmc_goldprice request...")

    return btmc_goldprice()


@mcp.tool()
async def get_vcb_exchange_rate(date: str = None):
    """
    Truy xuất tỷ giá ngoại tệ từ Vietcombank.
    Retrieve exchange rates from Vietcombank.
    Args:
    - date (tùy chọn): Date in format YYYY-MM-DD. 
    If left blank, the current date will be used.
    """
    logging.info("Processing vcb_exchange_rate request...")

    return vcb_exchange_rate(date=date)
