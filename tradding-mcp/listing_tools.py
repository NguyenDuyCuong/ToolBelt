"""
Listing / exchange / industries related MCP tools (extracted from original `main.py`).
"""
import logging
from typing import Literal

from mcp_instance import mcp
from vnstock.explorer.vci.listing import Listing as VCIListing


@mcp.tool()
async def all_symbols(show_log: bool = False):
    """
    Truy xuất danh sách toàn. bộ mã và tên các cổ phiếu trên thị trường Việt Nam.
    Retrieve all symbols (filtered to STOCK).

    Tham số:        
        - show_log (tùy chọn): Hiển thị thông tin log giúp debug dễ dàng. Mặc định là False.
    """
    logging.info("Processing all_symbols request...")

    listing = VCIListing()
    return listing.all_symbols(show_log=show_log)


@mcp.tool()
async def symbols_by_exchange(lang: str = "vi", show_log: bool = False):
    """
    Truy xuất danh sách mã và tên các cổ phiếu theo sàn giao dịch trên thị trường Việt Nam.
    Retrieve symbols by exchange/board.

    Tham số:
        - lang (tùy chọn): Ngôn ngữ hiển thị. Mặc định là 'vi'.
        - show_log (tùy chọn): Hiển thị thông tin log giúp debug dễ dàng. Mặc định là False
    """
    logging.info("Processing symbol_by_exchange request...")

    listing = VCIListing()
    return listing.symbols_by_exchange(lang=lang, show_log=show_log)


@mcp.tool()
async def symbols_by_group(group: str = "VN30", show_log: bool = False):
    """
    Retrieve symbols by predefined group (VN30, HNX30, CW, etc.).
    Liệt kê tất cả mã chứng khoán theo nhóm phân loại.
        HOSE, HNX, UPCOM
        VN30, VN100, HNX30
        VNMidCap, VNSmallCap, VNAllShare, HNXCon, HNXFin, HNXLCap, HNXMSCap, HNXMan,
        ETF
        FU_INDEX (mã chỉ số hợp đồng tương lai)
        CW (chứng quyền)
    Tham số:
        - group (tùy chọn): Tên nhóm cổ phiếu. Mặc định là 'VN30'.
        - show_log (tùy chọn): Hiển thị thông tin log. Mặc định là False.
    """
    logging.info("Processing symbol_by_group request...")

    listing = VCIListing()
    return listing.symbols_by_group(group=group, show_log=show_log)


@mcp.tool()
async def symbols_by_industries(language: str = "vi", show_log: bool = False):
    """
    Truy xuất danh sách mã và tên các cổ phiếu theo ngành nghề trên thị trường Việt Nam.
    Retrieve symbols by industries.

    Tham số:
        - lang (tùy chọn): Ngôn ngữ hiển thị. Mặc định là 'vi'.
        - show_log (tùy chọn): Hiển thị thông tin log giúp debug dễ dàng. Mặc định là False.
    """
    logging.info("Processing symbol_by_industries request...")

    listing = VCIListing()
    return listing.symbols_by_industries(lang=language, show_log=show_log)


@mcp.tool()
async def industries_icb(show_log: bool = False):
    """
    Truy xuất danh sách ngành nghề theo chuẩn ICB trên thị trường Việt Nam.
    Retrieve industries by ICB classification.

    Tham số:
        - show_log (tùy chọn): Hiển thị thông tin log giúp debug dễ dàng. Mặc định là False.
    """
    logging.info("Processing industries_icb request...")

    listing = VCIListing()
    return listing.industries_icb(show_log=show_log)
