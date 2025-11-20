"""
Truy xuất cổ phiếu thị trường Việt Nam.
"""

import asyncio
import logging
from mcp.server.fastmcp import FastMCP
from vnstock import Listing, Company

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

    company = Company(symbol=symbol, source="TCBS")
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

    company = Company(symbol=symbol, source="TCBS")
    return company.shareholders()


@mcp.tool()
async def officers(symbol: str, filter_by: str = "all"):
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

    company = Company(symbol=symbol, source="TCBS")
    return company.officers(filter_by=filter_by)


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
