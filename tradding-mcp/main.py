"""
Truy xuất cổ phiếu thị trường Việt Nam.
"""

import asyncio
import logging
from mcp.server.fastmcp import FastMCP
from vnstock import Listing

# Initialize FastMCP server
mcp = FastMCP("tradding-mcp")


@mcp.tool()
async def all_symbols(show_log=False, to_df=True):
    """
    Truy xuất danh sách toàn. bộ mã và tên các cổ phiếu trên thị trường Việt Nam.

    Tham số:
        - show_log (tùy chọn): Hiển thị thông tin log giúp debug dễ dàng. Mặc định là False.
        - to_df (tùy chọn): Chuyển đổi dữ liệu danh sách mã cổ phiếu trả về dưới dạng DataFrame. Mặc định là True. Đặt là False để trả về dữ liệu dạng JSON.
    """
    logging.info("Processing all_symbols request...")

    listing = Listing()
    return listing.all_symbols(show_log=show_log, to_df=to_df)


async def main():
    await mcp.run_sse_async()


if __name__ == "__main__":
    asyncio.run(main())
