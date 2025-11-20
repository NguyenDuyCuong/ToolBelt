"""
Finance-related MCP tools for financial reports (Báo cáo tài chính).
Supports both VCI and TCBS data sources.
"""

import logging
from typing import Literal

from vnstock import Vnstock, Finance
from vnstock.explorer.vci import Finance as VCIFinance
from vnstock.explorer.tcbs import Finance as TCBSFinance


from mcp_instance import mcp


# ============================================================================
# VCI SOURCE - Financial Reports
# ============================================================================


@mcp.tool()
async def income_statement_vci(
    symbol: str,
    period: Literal["year", "quarter"] = "year",
    lang: Literal["vi", "en"] = "vi",
    dropna: bool = False,
):
    """
    Trích xuất dữ liệu báo cáo kết quả kinh doanh cho một công ty từ nguồn VCI.

    Báo cáo kết quả kinh doanh hiển thị doanh thu, chi phí và lợi nhuận của công ty
    trong một kỳ báo cáo cụ thể.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất dữ liệu (ví dụ: 'VCI', 'VNM')
        - period: Kỳ báo cáo - 'year' (báo cáo năm) hoặc 'quarter' (báo cáo quý)
        - lang: Ngôn ngữ dữ liệu - 'vi' (Tiếng Việt) hoặc 'en' (Tiếng Anh)
        - dropna: Loại bỏ các dòng không chứa dữ liệu hoặc chỉ chứa giá trị 0

    Đơn vị: đồng
    Trả về: DataFrame chứa báo cáo kết quả kinh doanh
    """
    logging.info("Processing income_statement_vci for %s...", symbol)

    finance = VCIFinance(symbol=symbol)
    return finance.income_statement(period=period, lang=lang, dropna=dropna)


@mcp.tool()
async def balance_sheet_vci(
    symbol: str,
    period: Literal["year", "quarter"] = "year",
    lang: Literal["vi", "en"] = "vi",
    dropna: bool = False,
):
    """
    Truy xuất bảng cân đối kế toán (Balance Sheet) từ nguồn VCI.

    Bảng cân đối kế toán hiển thị tài sản, nợ phải trả và vốn chủ sở hữu của công ty
    tại một thời điểm cụ thể.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất dữ liệu (ví dụ: 'VCI', 'VNM')
        - period: Kỳ báo cáo - 'year' (báo cáo năm) hoặc 'quarter' (báo cáo quý)
        - lang: Ngôn ngữ dữ liệu - 'vi' (Tiếng Việt) hoặc 'en' (Tiếng Anh)
        - dropna: Loại bỏ các dòng không chứa dữ liệu hoặc chỉ chứa giá trị 0

    Đơn vị: đồng
    Trả về: DataFrame chứa bảng cân đối kế toán
    """
    logging.info("Processing balance_sheet_vci for %s...", symbol)


    finance = VCIFinance(symbol=symbol)
    return finance.balance_sheet(period=period, lang=lang, dropna=dropna)


@mcp.tool()
async def cash_flow_vci(
    symbol: str,
    period: Literal["year", "quarter"] = "year",
    lang: Literal["vi", "en"] = "vi",
    dropna: bool = False,
):
    """
    Truy xuất báo cáo lưu chuyển tiền tệ (Cash Flow) từ nguồn VCI.

    Báo cáo lưu chuyển tiền tệ hiển thị các dòng tiền vào và tiền ra từ hoạt động
    kinh doanh, đầu tư và tài chính của công ty.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất dữ liệu (ví dụ: 'VCI', 'VNM')
        - period: Kỳ báo cáo - 'year' (báo cáo năm) hoặc 'quarter' (báo cáo quý)
        - lang: Ngôn ngữ dữ liệu - 'vi' (Tiếng Việt) hoặc 'en' (Tiếng Anh)
        - dropna: Loại bỏ các dòng không chứa dữ liệu hoặc chỉ chứa giá trị 0

    Đơn vị: đồng
    Trả về: DataFrame chứa báo cáo lưu chuyển tiền tệ
    """
    logging.info("Processing cash_flow_vci for %s...", symbol)

    finance = VCIFinance(symbol=symbol)
    return finance.cash_flow(period=period, lang=lang, dropna=dropna)


@mcp.tool()
async def financial_ratio_vci(
    symbol: str,
    period: Literal["year", "quarter"] = "year",
    lang: Literal["vi", "en"] = "vi",
    dropna: bool = False,
):
    """
    Truy xuất chỉ số tài chính (Financial Ratios) từ nguồn VCI.

    Chỉ số tài chính bao gồm các chỉ tiêu định giá (P/E, P/B, P/S), chỉ tiêu khả
    năng sinh lợi (ROE, ROA), chỉ tiêu hiệu quả hoạt động và chỉ tiêu cơ cấu nguồn vốn.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất dữ liệu (ví dụ: 'VCI', 'VNM')
        - period: Kỳ báo cáo - 'year' (báo cáo năm) hoặc 'quarter' (báo cáo quý)
        - lang: Ngôn ngữ dữ liệu - 'vi' (Tiếng Việt) hoặc 'en' (Tiếng Anh)
        - dropna: Loại bỏ các dòng không chứa dữ liệu hoặc chỉ chứa giá trị 0

    Trả về: DataFrame chứa các chỉ số tài chính
    """
    logging.info("Processing financial_ratio_vci for %s...", symbol)

    finance = VCIFinance(symbol=symbol)
    return finance.ratio(period=period, lang=lang, dropna=dropna)


# ============================================================================
# TCBS SOURCE - Financial Reports
# ============================================================================


@mcp.tool()
async def income_statement_tcbs(
    symbol: str,
    period: Literal["year", "quarter"] = "year",
):
    """
    Truy xuất báo cáo kết quả kinh doanh (Income Statement) từ nguồn TCBS.

    Báo cáo kết quả kinh doanh hiển thị doanh thu, chi phí và lợi nhuận của công ty
    trong một kỳ báo cáo cụ thể.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất dữ liệu (ví dụ: 'VCI', 'VNM')
        - period: Kỳ báo cáo - 'year' (báo cáo năm) hoặc 'quarter' (báo cáo quý)

    Đơn vị: Tỷ đồng
    Trả về: DataFrame chứa báo cáo kết quả kinh doanh
    """
    logging.info("Processing income_statement_tcbs for %s...", symbol)

    finance = TCBSFinance(symbol=symbol)
    return finance.income_statement(period=period)


@mcp.tool()
async def balance_sheet_tcbs(
    symbol: str,
    period: Literal["year", "quarter"] = "year",
):
    """
    Truy xuất bảng cân đối kế toán (Balance Sheet) từ nguồn TCBS.

    Bảng cân đối kế toán hiển thị tài sản, nợ phải trả và vốn chủ sở hữu của công ty
    tại một thời điểm cụ thể.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất dữ liệu (ví dụ: 'VCI', 'VNM')
        - period: Kỳ báo cáo - 'year' (báo cáo năm) hoặc 'quarter' (báo cáo quý)

    Đơn vị: Tỷ đồng
    Trả về: DataFrame chứa bảng cân đối kế toán
    """
    logging.info("Processing balance_sheet_tcbs for %s...", symbol)

    stock = Vnstock().stock(symbol=symbol, source="TCBS")
    finance = stock.finance
    return finance.balance_sheet(period=period)


@mcp.tool()
async def cash_flow_tcbs(
    symbol: str,
    period: Literal["year", "quarter"] = "year",
):
    """
    Truy xuất báo cáo lưu chuyển tiền tệ (Cash Flow) từ nguồn TCBS.

    Báo cáo lưu chuyển tiền tệ hiển thị các dòng tiền vào và tiền ra từ hoạt động
    kinh doanh, đầu tư và tài chính của công ty.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất dữ liệu (ví dụ: 'VCI', 'VNM')
        - period: Kỳ báo cáo - 'year' (báo cáo năm) hoặc 'quarter' (báo cáo quý)

    Đơn vị: Tỷ đồng
    Trả về: DataFrame chứa báo cáo lưu chuyển tiền tệ
    """
    logging.info("Processing cash_flow_tcbs for %s...", symbol)

    stock = Vnstock().stock(symbol=symbol, source="TCBS")
    finance = stock.finance
    return finance.cash_flow(period=period)


@mcp.tool()
async def financial_ratio_tcbs(
    symbol: str,
    period: Literal["year", "quarter"] = "year",
    get_all: bool = True,
):
    """
    Truy xuất chỉ số tài chính (Financial Ratios) từ nguồn TCBS.

    Chỉ số tài chính bao gồm các chỉ tiêu định giá (P/E, P/B), chỉ tiêu khả
    năng sinh lợi (ROE, ROA), và các chỉ tiêu khác.

    Tham số:
        - symbol: Mã cổ phiếu cần truy xuất dữ liệu (ví dụ: 'VCI', 'VNM')
        - period: Kỳ báo cáo - 'year' (báo cáo năm) hoặc 'quarter' (báo cáo quý)
        - get_all: Trả về toàn bộ các chỉ số có trong dữ liệu (True) hay báo cáo rút gọn (False)

    Trả về: DataFrame chứa các chỉ số tài chính
    """
    logging.info("Processing financial_ratio_tcbs for %s...", symbol)

    stock = Vnstock().stock(symbol=symbol, source="TCBS")
    finance = stock.finance
    return finance.ratio(period=period, get_all=get_all)
