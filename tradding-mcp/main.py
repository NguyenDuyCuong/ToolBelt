"""
Truy xuất cổ phiếu thị trường Việt Nam.
"""

import asyncio
from typing import Literal
import logging
from mcp.server.fastmcp import FastMCP
from vnstock import Listing
from vnstock.explorer.tcbs.company import Company as TCBSCompany
from vnstock.explorer.vci.company import Company as VCICompany

# Initialize FastMCP server
mcp = FastMCP("tradding-mcp")


@mcp.tool()
async def overview(symbol: str):
    """
    Cung cấp tổng quan về công ty cổ phần trên thị trường Việt Nam.
    Retrieve company overview data.

    Trả về thông tin cơ bản của các công ty bao gồm mã cổ phiếu, tên công ty, ngành nghề, sàn giao dịch, v.v.
    """
    logging.info("Processing overview request...")

    company = VCICompany(symbol=symbol)
    return company.overview()


@mcp.tool()
async def shareholders(symbol: str):
    """
    Truy xuất thông tin cổ đông lớn của một cổ phiếu cụ thể trên thị trường Việt Nam.
    Retrieve company shareholders data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin cổ đông lớn.
    """
    logging.info("Processing shareholders request...")

    company = VCICompany(symbol=symbol)
    return company.shareholders()


@mcp.tool()
async def officers(symbol: str, filter_by: Literal['working', "all", 'resigned']= 'working'):
    """
    Truy xuất thông tin ban lãnh đạo của một cổ phiếu cụ thể trên thị trường Việt Nam.
    Retrieve company officers data. Supports kwargs like filter_by='working'|'resigned'|'all'.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin ban lãnh đạo.
        - filter_by: Lọc dữ liệu trả về theo danh sách lãnh đạo đang làm việc hay đã từ nhiệm.
            working: đang làm việc (mặc định)
            resigned: đã nghỉ.
            all: toàn bộ
    """
    logging.info("Processing officers request...")

    company = VCICompany(symbol=symbol)
    return company.officers(filter_by=filter_by)


@mcp.tool()
async def subsidiaries(symbol: str, filter_by: Literal["all", "subsidiary", "affiliate"] = "all"):
    """
    Truy xuất thông tin công ty con của một cổ phiếu cụ thể trên thị trường Việt Nam.
    Retrieve company subsidiaries data. Supports kwargs like filter_by='all'|'subsidiary'.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin công ty con.
        - filter_by (str): Lọc công ty con hoặc công ty liên kết.
            'all': Lọc tất cả.
            'subsidiary': Lọc công ty con.
            'affiliate': Lọc công ty liên kết
    """
    logging.info("Processing subsidiaries request...")

    company = VCICompany(symbol=symbol)
    return company.subsidiaries(filter_by=filter_by)


@mcp.tool()
async def events(symbol: str):
    """
    Truy xuất thông tin sự kiện của một cổ phiếu cụ thể trên thị trường Việt Nam.
    Retrieve company events data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin sự kiện.
    """
    logging.info("Processing events request...")

    company = VCICompany(symbol=symbol)
    return company.events()


@mcp.tool()
async def news(symbol: str):
    """
    Truy xuất tin tức liên quan đến công ty.
    Retrieve company news data.
    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin tin tức.
    """
    logging.info("Processing news request...")

    company = VCICompany(symbol=symbol)
    return company.news()


@mcp.tool()
async def reports(symbol: str):
    """
    Truy xuất báo cáo phân tích về công ty.
    Retrieve company financial reports data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin báo cáo tài chính.
    """
    logging.info("Processing reports request...")

    company = VCICompany(symbol=symbol)
    return company.reports()


@mcp.tool()
async def ratio_summary(symbol: str):
    """
    Truy xuất tóm tắt các chỉ số tài chính quan trọng của công ty.
    Retrieve company financial ratio summary data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin tóm tắt các chỉ số tài chính.
    """
    logging.info("Processing ratio_summary request...")

    company = VCICompany(symbol=symbol)
    return company.ratio_summary()


@mcp.tool()
async def trading_stats(symbol: str):
    """
    Truy xuất thống kê giao dịch của công ty.
    Retrieve company trading statistics data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin thống kê giao dịch.
    """
    logging.info("Processing trading_stats request...")

    company = VCICompany(symbol=symbol)
    return company.trading_stats()


@mcp.tool()
async def all_symbols(show_log=False, to_df=True):
    """
    Truy xuất danh sách toàn. bộ mã và tên các cổ phiếu trên thị trường Việt Nam.
    Retrieve all symbols (filtered to STOCK).

    Tham số:
        - show_log (tùy chọn): Hiển thị thông tin log giúp debug dễ dàng. Mặc định là False.
        - to_df (tùy chọn): Chuyển đổi dữ liệu danh sách mã cổ phiếu trả về dưới dạng DataFrame. Mặc định là True. Đặt là False để trả về dữ liệu dạng JSON.
    """
    logging.info("Processing all_symbols request...")

    listing = Listing()
    return listing.all_symbols(show_log=show_log, to_df=to_df)


async def main():
    """
    Run the FastMCP server with SSE support.
    """
    await mcp.run_sse_async()


if __name__ == "__main__":
    asyncio.run(main())
