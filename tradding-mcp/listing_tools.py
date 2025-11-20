"""
Listing / exchange / industries related MCP tools (extracted from original `main.py`).
"""
import logging
from typing import Literal

from vnstock.explorer.vci.listing import Listing as VCIListing
from vnstock.explorer.msn.listing import Listing as MSNListing
from mcp_instance import mcp


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


@mcp.tool()
async def all_indices():
    """
    Truy xuất danh sách tất cả các chỉ số thị trường trên sàn chứng khoán Việt Nam.
    Retrieve all market indices.

    Tham số:        
    """
    logging.info("Processing all_indices request...")

    listing = VCIListing()
    return listing.all_indices()


@mcp.tool()
async def indices_by_group(group: Literal["HOSE Indices", "Sector Indices", "Investment Indices", "VNX Indices"] = "HOSE Indices"):
    """
    Lấy danh sách chỉ số theo nhóm tiêu chuẩn hóa.
    Retrieve market indices by group.

    Tham số:
        - group (tùy chọn): Tên nhóm chỉ số. 
            HOSE Indices: Các chỉ số chính của sàn HOSE (VN30, VN100, v.v.)
            Sector Indices: Các chỉ số ngành (VNIT, VNIND, VNCONS, v.v.)
            Investment Indices: Các chỉ số đầu tư (VNDIAMOND, VNFINLEAD, v.v.)
            VNX Indices: Các chỉ số của sàn HNX (VNX50, VNXALL)
    """
    logging.info("Processing indices_by_group request...")

    listing = VCIListing()
    return listing.indices_by_group(group=group)


@mcp.tool()
async def search_symbol_id(query: str, locale: str = None, limit: int = 10, show_log: bool = False):
    """
    Truy xuất danh sách toàn bộ mã và tên các cổ phiếu từ thị trường.
    Search for a stock symbol and return detailed information.

    Tham số:
        - query (bắt buộc): Từ khóa tìm kiếm mã cổ phiếu.
        - locale (tùy chọn): Ngôn ngữ mục tiêu, đồng thời sử dụng để lọc kết quả, ví dụ 'vi-vn', 'en-us'. Mặc định là None.
        - limit (tùy chọn): Giới hạn số kết quả. Mặc định là 10.
        - show_log (tùy chọn): Hiển thị thông tin log giúp debug dễ dàng. Mặc định là False.
    """
    logging.info("Processing search_symbol_id request...")

    listing = MSNListing()
    return listing.search_symbol_id(query=query, locale=locale, limit=limit, show_log=show_log)
