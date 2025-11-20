"""
Fund-related tools for MCP.
"""

import logging

from vnstock import Fund
from mcp_instance import mcp


@mcp.tool()
async def fund_listing(fund_type: str = ""):
    """
    Truy xuất danh sách quỹ đầu tư trên thị trường Việt Nam.
    Retrieve fund listing.

    Tham số:
        - fund_type (str, không bắt buộc): nhóm phân loại quỹ, mặc định là rỗng để liệt kê tất cả quỹ. Các giá trị có thể sử dụng bao gồm:
            BALANCED: Quỹ cân bằng
            BOND: Quỹ trái phiếu
            STOCK: Quỹ cổ phiếu
            "": string rỗng (mặc định) - Tất cả quỹ
    """
    logging.info("Processing fund listing request...")

    fund = Fund()
    return fund.listing(fund_type=fund_type)


@mcp.tool()
async def fund_filter(symbol: str = ""):
    """
    Truy xuất danh sách quỹ theo tên viết tắt (short_name) và mã id của quỹ. Mặc định là rỗng để liệt kê tất cả các quỹ.
    Filter funds by category.

    Tham số:
        - symbol (str, bắt buộc): Tên viết tắt của quỹ cần tìm kiếm. Nhập 1 phần tên để liệt kê các kết quả trùng khớp.
    """
    logging.info("Processing fund filter request...")

    fund = Fund()
    return fund.filter(symbol=symbol)


@mcp.tool()
async def fund_nav_report(symbol: str):
    """
    Báo cáo tăng trưởng NAV của quỹ đầu tư.

    Tham số:
        - symbol (str, bắt buộc): Tên viết tắt của quỹ cần tìm kiếm. 
        Nhập 1 phần tên để liệt kê các kết quả trùng khớp.
    """
    logging.info("Processing fund NAV report request...")

    fund = Fund()
    return fund.details.nav_report(symbol=symbol)


@mcp.tool()
async def fund_top_holding(symbol: str):
    """
    Danh mục đầu tư lớn nhất của quỹ đầu tư.

    Tham số:
        - symbol (str, bắt buộc): Tên viết tắt của quỹ cần tìm kiếm. 
        Nhập 1 phần tên để liệt kê các kết quả trùng khớp.
    """
    logging.info("Processing fund top holdings request...")

    fund = Fund()
    return fund.details.top_holding(symbol=symbol)


@mcp.tool()
async def fund_industry_holding(symbol: str):
    """
    Phân bổ theo ngành của quỹ đầu tư.

    Tham số:
        - symbol (str, bắt buộc): Tên viết tắt của quỹ cần tìm kiếm. 
        Nhập 1 phần tên để liệt kê các kết quả trùng khớp.
    """
    logging.info("Processing fund industry holdings request...")

    fund = Fund()
    return fund.details.industry_holding(symbol=symbol)


@mcp.tool()
async def fund_asset_holding(symbol: str):
    """
    Phân bổ theo loại tài sản của quỹ đầu tư.

    Tham số:
        - symbol (str, bắt buộc): Tên viết tắt của quỹ cần tìm kiếm. 
        Nhập 1 phần tên để liệt kê các kết quả trùng khớp.
    """
    logging.info("Processing fund asset holdings request...")

    fund = Fund()
    return fund.details.asset_holding(symbol=symbol)

