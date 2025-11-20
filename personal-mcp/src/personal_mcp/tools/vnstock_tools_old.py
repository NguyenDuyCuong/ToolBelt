"""VNStock MCP tools registration.

Registers all vnstock wrapper functions as MCP tools with proper parameter
handling, response formatting, and JSON serialization.
"""

import json
from typing import Any, Optional

import pandas as pd

from src.personal_mcp.adapters.vnstock_adapter import get_vnstock_adapter


def setup_vnstock_tools(server) -> None:
    """Set up all VNStock tools for the MCP server.

    Args:
        server: FastMCP server instance.
    """
    adapter = get_vnstock_adapter()

    # =========================================================================
    # LISTING TOOLS (10 methods)
    # =========================================================================

    @server.tool
    async def listing_all_bonds(params: Optional[dict] = None) -> str:
        """Get all bonds.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with all bonds data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_all_bonds(**kwargs)
            # Convert DataFrame to JSON if applicable
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def listing_all_covered_warrant(params: Optional[dict] = None) -> str:
        """Get all covered warrants.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with covered warrants data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_all_covered_warrant(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def listing_all_future_indices(params: Optional[dict] = None) -> str:
        """Get all future indices.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with future indices data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_all_future_indices(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def listing_all_government_bonds(params: Optional[dict] = None) -> str:
        """Get all government bonds.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with government bonds data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_all_government_bonds(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def listing_all_symbols(params: Optional[dict] = None) -> str:
        """Get all symbols.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with all symbols data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_all_symbols(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def listing_history(params: Optional[dict] = None) -> str:
        """Get listing history.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with listing history data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_history(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def listing_industries_icb(params: Optional[dict] = None) -> str:
        """Get industries by ICB classification.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with industries data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_industries_icb(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def listing_symbols_by_exchange(params: Optional[dict] = None) -> str:
        """Get symbols by exchange.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with symbols by exchange data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_symbols_by_exchange(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def listing_symbols_by_group(params: Optional[dict] = None) -> str:
        """Get symbols by group.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with symbols by group data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_symbols_by_group(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def listing_symbols_by_industries(params: Optional[dict] = None) -> str:
        """Get symbols by industries.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with symbols by industries data.
        """
        try:
            kwargs = params or {}
            result = adapter.listing_symbols_by_industries(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    # =========================================================================
    # QUOTE TOOLS (3 methods)
    # =========================================================================

    @server.tool
    async def quote_history(
        symbol: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        interval: str = "1D",
    ) -> str:
        """Get quote history for a symbol.

        Args:
            symbol: Stock symbol.
            start: Start date (YYYY-MM-DD).
            end: End date (YYYY-MM-DD).
            interval: Time interval (default: 1D).

        Returns:
            JSON string with history data.
        """
        try:
            result = adapter.quote_history(symbol=symbol, start=start, end=end, interval=interval)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def quote_intraday(
        symbol: Optional[str] = None, page_size: int = 100, page: int = 1
    ) -> str:
        """Get intraday quote data.

        Args:
            symbol: Stock symbol.
            page_size: Records per page (default: 100).
            page: Page number (default: 1).

        Returns:
            JSON string with intraday data.
        """
        try:
            result = adapter.quote_intraday(symbol=symbol, page_size=page_size, page=page)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def quote_price_depth(symbol: Optional[str] = None) -> str:
        """Get price depth data.

        Args:
            symbol: Stock symbol.

        Returns:
            JSON string with price depth data.
        """
        try:
            result = adapter.quote_price_depth(symbol=symbol)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    # =========================================================================
    # TRADING TOOLS (9 methods)
    # =========================================================================

    @server.tool
    async def trading_foreign_trade(params: Optional[dict] = None) -> str:
        """Get foreign trade data.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with foreign trade data.
        """
        try:
            kwargs = params or {}
            result = adapter.trading_foreign_trade(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def trading_history(params: Optional[dict] = None) -> str:
        """Get trading history.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with trading history data.
        """
        try:
            kwargs = params or {}
            result = adapter.trading_history(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def trading_insider_deal(params: Optional[dict] = None) -> str:
        """Get insider deals.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with insider deals data.
        """
        try:
            kwargs = params or {}
            result = adapter.trading_insider_deal(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def trading_order_stats(params: Optional[dict] = None) -> str:
        """Get order statistics.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with order statistics data.
        """
        try:
            kwargs = params or {}
            result = adapter.trading_order_stats(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def trading_price_board(params: Optional[dict] = None) -> str:
        """Get price board data.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with price board data.
        """
        try:
            kwargs = params or {}
            result = adapter.trading_price_board(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def trading_price_history(params: Optional[dict] = None) -> str:
        """Get price history.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with price history data.
        """
        try:
            kwargs = params or {}
            result = adapter.trading_price_history(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def trading_prop_trade(params: Optional[dict] = None) -> str:
        """Get proprietary trade data.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with proprietary trade data.
        """
        try:
            kwargs = params or {}
            result = adapter.trading_prop_trade(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def trading_side_stats(params: Optional[dict] = None) -> str:
        """Get side statistics.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with side statistics data.
        """
        try:
            kwargs = params or {}
            result = adapter.trading_side_stats(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def trading_trading_stats(params: Optional[dict] = None) -> str:
        """Get trading statistics.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with trading statistics data.
        """
        try:
            kwargs = params or {}
            result = adapter.trading_trading_stats(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    # =========================================================================
    # FINANCE TOOLS (5 methods)
    # =========================================================================

    @server.tool
    async def finance_balance_sheet(params: Optional[dict] = None) -> str:
        """Get balance sheet data.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with balance sheet data.
        """
        try:
            kwargs = params or {}
            result = adapter.finance_balance_sheet(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def finance_cash_flow(params: Optional[dict] = None) -> str:
        """Get cash flow data.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with cash flow data.
        """
        try:
            kwargs = params or {}
            result = adapter.finance_cash_flow(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def finance_history(params: Optional[dict] = None) -> str:
        """Get finance history.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with finance history data.
        """
        try:
            kwargs = params or {}
            result = adapter.finance_history(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def finance_income_statement(params: Optional[dict] = None) -> str:
        """Get income statement data.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with income statement data.
        """
        try:
            kwargs = params or {}
            result = adapter.finance_income_statement(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def finance_ratio(params: Optional[dict] = None) -> str:
        """Get financial ratios.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with financial ratios data.
        """
        try:
            kwargs = params or {}
            result = adapter.finance_ratio(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    # =========================================================================
    # COMPANY TOOLS (8 methods)
    # =========================================================================

    @server.tool
    async def company_affiliate(params: Optional[dict] = None) -> str:
        """Get company affiliates.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with affiliate data.
        """
        try:
            kwargs = params or {}
            result = adapter.company_affiliate(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def company_events(params: Optional[dict] = None) -> str:
        """Get company events.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with company events data.
        """
        try:
            kwargs = params or {}
            result = adapter.company_events(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def company_history(params: Optional[dict] = None) -> str:
        """Get company history.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with company history data.
        """
        try:
            kwargs = params or {}
            result = adapter.company_history(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def company_news(params: Optional[dict] = None) -> str:
        """Get company news.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with company news data.
        """
        try:
            kwargs = params or {}
            result = adapter.company_news(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def company_officers(params: Optional[dict] = None) -> str:
        """Get company officers.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with company officers data.
        """
        try:
            kwargs = params or {}
            result = adapter.company_officers(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def company_overview(params: Optional[dict] = None) -> str:
        """Get company overview.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with company overview data.
        """
        try:
            kwargs = params or {}
            result = adapter.company_overview(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def company_shareholders(params: Optional[dict] = None) -> str:
        """Get company shareholders.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with company shareholders data.
        """
        try:
            kwargs = params or {}
            result = adapter.company_shareholders(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def company_subsidiaries(params: Optional[dict] = None) -> str:
        """Get company subsidiaries.

        Args:
            params: Additional parameters dictionary.

        Returns:
            JSON string with company subsidiaries data.
        """
        try:
            kwargs = params or {}
            result = adapter.company_subsidiaries(**kwargs)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    # =========================================================================
    # FUND TOOLS (7 methods)
    # =========================================================================

    @server.tool
    async def fund_asset_holding(fund_id: int = 23) -> str:
        """Get fund asset holdings.

        Args:
            fund_id: Fund ID (default: 23).

        Returns:
            JSON string with asset holding data.
        """
        try:
            result = adapter.fund_asset_holding(fund_id=fund_id)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def fund_filter(symbol: str = "") -> str:
        """Filter funds by symbol.

        Args:
            symbol: Fund symbol (optional).

        Returns:
            JSON string with filtered fund data.
        """
        try:
            result = adapter.fund_filter(symbol=symbol)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def fund_industry_holding(fund_id: int = 23) -> str:
        """Get fund industry holdings.

        Args:
            fund_id: Fund ID (default: 23).

        Returns:
            JSON string with industry holding data.
        """
        try:
            result = adapter.fund_industry_holding(fund_id=fund_id)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def fund_listing(fund_type: str = "") -> str:
        """Get fund listings.

        Args:
            fund_type: Fund type (optional).

        Returns:
            JSON string with fund listing data.
        """
        try:
            result = adapter.fund_listing(fund_type=fund_type)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def fund_nav_report(fund_id: int = 23) -> str:
        """Get fund NAV report.

        Args:
            fund_id: Fund ID (default: 23).

        Returns:
            JSON string with NAV report data.
        """
        try:
            result = adapter.fund_nav_report(fund_id=fund_id)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def fund_top_holding(fund_id: int = 23) -> str:
        """Get fund top holdings.

        Args:
            fund_id: Fund ID (default: 23).

        Returns:
            JSON string with top holding data.
        """
        try:
            result = adapter.fund_top_holding(fund_id=fund_id)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    # =========================================================================
    # SCREENER TOOLS (1 method)
    # =========================================================================

    @server.tool
    async def screener_stock(
        params: Optional[dict] = None, limit: int = 50, id: Optional[str] = None, lang: str = "vi"
    ) -> str:
        """Screen stocks based on parameters.

        Args:
            params: Filter parameters dictionary.
            limit: Maximum number of results (default: 50).
            id: Screener ID (optional).
            lang: Language (default: 'vi').

        Returns:
            JSON string with screened stock data.
        """
        try:
            result = adapter.screener_stock(params=params, limit=limit, id=id, lang=lang)
            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    # =========================================================================
    # VNSTOCK ROOT TOOLS (5 methods)
    # =========================================================================

    @server.tool
    async def vnstock_stock(symbol: Optional[str] = None, source: Optional[str] = None) -> str:
        """Get stock components.

        Args:
            symbol: Stock symbol.
            source: Data source.

        Returns:
            JSON string with stock components.
        """
        try:
            result = adapter.vnstock_stock(symbol=symbol, source=source)
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def vnstock_fund(source: str = "FMARKET") -> str:
        """Get fund components.

        Args:
            source: Data source (default: 'FMARKET').

        Returns:
            JSON string with fund components.
        """
        try:
            result = adapter.vnstock_fund(source=source)
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def vnstock_crypto(symbol: Optional[str] = "BTC", source: Optional[str] = "MSN") -> str:
        """Get crypto components.

        Args:
            symbol: Crypto symbol (default: 'BTC').
            source: Data source (default: 'MSN').

        Returns:
            JSON string with crypto components.
        """
        try:
            result = adapter.vnstock_crypto(symbol=symbol, source=source)
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def vnstock_fx(symbol: Optional[str] = "EURUSD", source: Optional[str] = "MSN") -> str:
        """Get forex components.

        Args:
            symbol: Forex symbol (default: 'EURUSD').
            source: Data source (default: 'MSN').

        Returns:
            JSON string with forex components.
        """
        try:
            result = adapter.vnstock_fx(symbol=symbol, source=source)
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @server.tool
    async def vnstock_world_index(symbol: Optional[str] = "DJI", source: Optional[str] = "MSN") -> str:
        """Get world index components.

        Args:
            symbol: Index symbol (default: 'DJI').
            source: Data source (default: 'MSN').

        Returns:
            JSON string with world index components.
        """
        try:
            result = adapter.vnstock_world_index(symbol=symbol, source=source)
            return json.dumps({"data": str(result)})
        except Exception as e:
            return json.dumps({"error": str(e)})
