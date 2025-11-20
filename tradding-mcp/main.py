"""
Truy xuất cổ phiếu thị trường Việt Nam.
"""

import asyncio
from typing import Literal
import logging
from mcp.server.fastmcp import FastMCP
from vnstock import Listing, Company
from vnstock.explorer.tcbs.company import Company as TCBSCompany
from vnstock.explorer.vci.company import Company as VCICompany

# Initialize FastMCP server
mcp = FastMCP("tradding-mcp")


@mcp.tool()
async def overview(symbol: str, source: Literal["VCI", "TCBS"] = "VCI"):
    """
    Cung cấp tổng quan về công ty cổ phần trên thị trường Việt Nam.
    Retrieve company overview data.

    Trả về thông tin cơ bản của các công ty bao gồm mã cổ phiếu, tên công ty, ngành nghề, sàn giao dịch, v.v.
    """
    logging.info("Processing overview request...")

    company = Company(symbol=symbol, source=source)
    return company.overview()


@mcp.tool()
async def profile(symbol: str):
    """
    Truy xuất thông tin mô tả công ty theo mã chứng khoán.
    Retrieve company profile data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin hồ sơ công ty.
    """
    logging.info("Processing profile request...")

    company = TCBSCompany(symbol=symbol)
    return company.profile()


@mcp.tool()
async def shareholders(symbol: str, source: Literal["VCI", "TCBS"] = "VCI"):
    """
    Truy xuất thông tin cổ đông lớn của một cổ phiếu cụ thể trên thị trường Việt Nam.
    Retrieve company shareholders data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin cổ đông lớn.
    """
    logging.info("Processing shareholders request...")

    company = Company(symbol=symbol, source=source)
    return company.shareholders()


@mcp.tool()
async def officers_vci(symbol: str, filter_by: Literal['working', "all", 'resigned']= 'working'):
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
async def officers_tcbs(symbol: str, page_size: int = 20, page: int = 0):
    """
    Truy xuất danh sách lãnh đạo của một công ty theo mã chứng khoán từ nguồn dữ liệu TCBS.
    Retrieve company officers data. 

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin ban lãnh đạo.
        - page_size (int): Số lượng lãnh đạo trên mỗi trang. Mặc định là 20.
        - page (int): Trang cần truy xuất thông tin. Mặc định là 0.
    """
    logging.info("Processing officers request...")

    company = TCBSCompany(symbol=symbol)
    return company.officers(page=page, page_size=page_size)


@mcp.tool()
async def subsidiaries_vci(symbol: str, filter_by: Literal["all", "subsidiary", "affiliate"] = "all"):
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
async def subsidiaries_tcbs(symbol: str, page_size: int = 100, page: int = 0):
    """
    Truy xuất thông tin các công ty con, công ty liên kết của một công ty theo mã chứng khoán từ nguồn dữ liệu TCBS.
    Retrieve company subsidiaries data.
    
    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin công ty con.
        - page_size (int): Số lượng công ty con trên mỗi trang. Mặc định là 100.
        - page (int): Trang cần truy xuất thông tin. Mặc định là 0.
    """
    logging.info("Processing subsidiaries request...")

    company = TCBSCompany(symbol=symbol)
    return company.subsidiaries(page=page, page_size=page_size)


@mcp.tool()
async def dividends(symbol: str, page_size: int = 15, page: int = 0):
    """
    Truy xuất lịch sử cổ tức của một công ty theo mã chứng khoán từ nguồn dữ liệu TCBS.
    Retrieve company dividends data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin cổ tức.
        - page_size (int): Số lượng kết quả trên mỗi trang. Mặc định là 15.
        - page (int): Trang cần truy xuất thông tin. Mặc định là 0.
    """
    logging.info("Processing dividends request...")

    company = TCBSCompany(symbol=symbol)
    return company.dividends(page=page, page_size=page_size)


@mcp.tool()
async def insider_deals(symbol: str, page_size: int = 20, page: int = 0):
    """
    Truy xuất thông tin giao dịch nội bộ của công ty theo mã chứng khoán từ nguồn dữ liệu TCBS.
    Retrieve company insider deals data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin giao dịch nội bộ.
        - page_size (int): Số lượng giao dịch trên mỗi trang. Mặc định là 20.
        - page (int): Trang cần truy xuất thông tin. Mặc định là 0.
    """
    logging.info("Processing insider_deals request...")

    company = TCBSCompany(symbol=symbol)
    return company.insider_deals(page=page, page_size=page_size)


@mcp.tool()
async def events(symbol: str, source: Literal["VCI", "TCBS"] = "VCI"):
    """
    Truy xuất thông tin sự kiện của một cổ phiếu cụ thể trên thị trường Việt Nam.
    Retrieve company events data.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin sự kiện.
    """
    logging.info("Processing events request...")

    company = Company(symbol=symbol, source=source)
    return company.events()


@mcp.tool()
async def news(symbol: str, source: Literal["VCI", "TCBS"] = "VCI"):
    """
    Truy xuất tin tức liên quan đến công ty.
    Retrieve company news data.
    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất thông tin tin tức.
    """
    logging.info("Processing news request...")

    company = Company(symbol=symbol, source=source)
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
