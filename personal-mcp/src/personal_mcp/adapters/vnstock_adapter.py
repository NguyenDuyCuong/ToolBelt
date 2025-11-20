"""VNStock adapter layer.

Wraps vnstock library functions to provide a clean, typed interface for MCP tools.
All methods here are pure adapters that delegate to vnstock library.
"""

from typing import Any, Optional

import pandas as pd
import vnstock
from fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)


class VNStockAdapter:
    """Adapter for vnstock library.

    Initializes vnstock classes and provides wrapper methods for all public functions.
    """

    def __init__(self) -> None:
        """Initialize vnstock adapter with singleton instances of each class.
        
        Note: Some classes require parameters, so they are initialized lazily.
        """
        self.listing = vnstock.Listing()
        self.quote: Optional[vnstock.Quote] = None  # Lazy - requires symbol
        self.trading = vnstock.Trading()
        self.finance: Optional[vnstock.Finance] = None  # Lazy - requires source and symbol
        self.company: Optional[vnstock.Company] = None  # Lazy - requires symbol
        self.fund = vnstock.Fund()
        self.screener = vnstock.Screener()
        self.vnstock_root = vnstock.Vnstock()

    # =========================================================================
    # LISTING METHODS (10 methods)
    # =========================================================================

    def listing_all_bonds(self, **kwargs: Any) -> Any:
        """Get all bonds.

        Args:
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.all_bonds(**kwargs)
            logger.info("listing_all_bonds completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_all_bonds: {e}")
            raise

    def listing_all_covered_warrant(self, **kwargs: Any) -> Any:
        """Get all covered warrants.

        Args:
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.all_covered_warrant(**kwargs)
            logger.info("listing_all_covered_warrant completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_all_covered_warrant: {e}")
            raise

    def listing_all_future_indices(self, **kwargs: Any) -> Any:
        """Get all future indices.

        Args:
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.all_future_indices(**kwargs)
            logger.info("listing_all_future_indices completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_all_future_indices: {e}")
            raise

    def listing_all_government_bonds(self, **kwargs: Any) -> Any:
        """Get all government bonds.

        Args:
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.all_government_bonds(**kwargs)
            logger.info("listing_all_government_bonds completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_all_government_bonds: {e}")
            raise

    def listing_all_symbols(self, *args: Any, **kwargs: Any) -> Any:
        """Get all symbols.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.all_symbols(*args, **kwargs)
            logger.info("listing_all_symbols completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_all_symbols: {e}")
            raise

    def listing_history(self, *args: Any, **kwargs: Any) -> Any:
        """Get listing history.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.history(*args, **kwargs)
            logger.info("listing_history completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_history: {e}")
            raise

    def listing_industries_icb(self, *args: Any, **kwargs: Any) -> Any:
        """Get industries by ICB classification.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.industries_icb(*args, **kwargs)
            logger.info("listing_industries_icb completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_industries_icb: {e}")
            raise

    def listing_symbols_by_exchange(self, *args: Any, **kwargs: Any) -> Any:
        """Get symbols by exchange.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.symbols_by_exchange(*args, **kwargs)
            logger.info("listing_symbols_by_exchange completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_symbols_by_exchange: {e}")
            raise

    def listing_symbols_by_group(self, *args: Any, **kwargs: Any) -> Any:
        """Get symbols by group.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.symbols_by_group(*args, **kwargs)
            logger.info("listing_symbols_by_group completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_symbols_by_group: {e}")
            raise

    def listing_symbols_by_industries(self, *args: Any, **kwargs: Any) -> Any:
        """Get symbols by industries.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.listing.symbols_by_industries(*args, **kwargs)
            logger.info("listing_symbols_by_industries completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in listing_symbols_by_industries: {e}")
            raise

    # =========================================================================
    # QUOTE METHODS (3 methods)
    # =========================================================================

    def quote_history(
        self,
        symbol: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        interval: str = "1D",
        **kwargs: Any,
    ) -> pd.DataFrame:
        """Get quote history for a symbol.

        Args:
            symbol: Stock symbol.
            start: Start date (format: YYYY-MM-DD).
            end: End date (format: YYYY-MM-DD).
            interval: Time interval (default: 1D).
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame with history data.
        """
        try:
            if symbol:
                quote = vnstock.Quote(symbol=symbol)
                result = quote.history(
                    symbol=symbol, start=start, end=end, interval=interval, **kwargs
                )
            else:
                result = self.quote.history(
                    symbol=symbol, start=start, end=end, interval=interval, **kwargs
                )
            logger.info(f"quote_history completed for symbol: {symbol}")
            return result
        except Exception as e:
            logger.error(f"Error in quote_history: {e}")
            raise

    def quote_intraday(
        self,
        symbol: Optional[str] = None,
        page_size: int = 100,
        page: int = 1,
        **kwargs: Any,
    ) -> pd.DataFrame:
        """Get intraday quote data.

        Args:
            symbol: Stock symbol.
            page_size: Number of records per page.
            page: Page number.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame with intraday data.
        """
        try:
            if symbol:
                quote = vnstock.Quote(symbol=symbol)
                result = quote.intraday(
                    symbol=symbol, page_size=page_size, page=page, **kwargs
                )
            else:
                result = self.quote.intraday(
                    symbol=symbol, page_size=page_size, page=page, **kwargs
                )
            logger.info(f"quote_intraday completed for symbol: {symbol}")
            return result
        except Exception as e:
            logger.error(f"Error in quote_intraday: {e}")
            raise

    def quote_price_depth(
        self, symbol: Optional[str] = None, **kwargs: Any
    ) -> pd.DataFrame:
        """Get price depth data.

        Args:
            symbol: Stock symbol.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame with price depth data.
        """
        try:
            if symbol:
                quote = vnstock.Quote(symbol=symbol)
                result = quote.price_depth(symbol=symbol, **kwargs)
            else:
                result = self.quote.price_depth(symbol=symbol, **kwargs)
            logger.info(f"quote_price_depth completed for symbol: {symbol}")
            return result
        except Exception as e:
            logger.error(f"Error in quote_price_depth: {e}")
            raise

    # =========================================================================
    # TRADING METHODS (9 methods)
    # =========================================================================

    def trading_foreign_trade(self, *args: Any, **kwargs: Any) -> Any:
        """Get foreign trade data.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.trading.foreign_trade(*args, **kwargs)
            logger.info("trading_foreign_trade completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in trading_foreign_trade: {e}")
            raise

    def trading_history(self, *args: Any, **kwargs: Any) -> Any:
        """Get trading history.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.trading.history(*args, **kwargs)
            logger.info("trading_history completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in trading_history: {e}")
            raise

    def trading_insider_deal(self, *args: Any, **kwargs: Any) -> Any:
        """Get insider deals.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.trading.insider_deal(*args, **kwargs)
            logger.info("trading_insider_deal completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in trading_insider_deal: {e}")
            raise

    def trading_order_stats(self, *args: Any, **kwargs: Any) -> Any:
        """Get order statistics.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.trading.order_stats(*args, **kwargs)
            logger.info("trading_order_stats completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in trading_order_stats: {e}")
            raise

    def trading_price_board(self, *args: Any, **kwargs: Any) -> Any:
        """Get price board data.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.trading.price_board(*args, **kwargs)
            logger.info("trading_price_board completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in trading_price_board: {e}")
            raise

    def trading_price_history(self, *args: Any, **kwargs: Any) -> Any:
        """Get price history.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.trading.price_history(*args, **kwargs)
            logger.info("trading_price_history completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in trading_price_history: {e}")
            raise

    def trading_prop_trade(self, *args: Any, **kwargs: Any) -> Any:
        """Get proprietary trade data.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.trading.prop_trade(*args, **kwargs)
            logger.info("trading_prop_trade completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in trading_prop_trade: {e}")
            raise

    def trading_side_stats(self, *args: Any, **kwargs: Any) -> Any:
        """Get side statistics.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.trading.side_stats(*args, **kwargs)
            logger.info("trading_side_stats completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in trading_side_stats: {e}")
            raise

    def trading_trading_stats(self, *args: Any, **kwargs: Any) -> Any:
        """Get trading statistics.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            result = self.trading.trading_stats(*args, **kwargs)
            logger.info("trading_trading_stats completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in trading_trading_stats: {e}")
            raise

    # =========================================================================
    # FINANCE METHODS (5 methods)
    # =========================================================================

    def finance_balance_sheet(self, *args: Any, **kwargs: Any) -> Any:
        """Get balance sheet data.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            # Finance requires source and symbol - need to create instance
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for finance_balance_sheet")
            finance = vnstock.Finance(source=source, symbol=symbol)
            result = finance.balance_sheet(*args, **kwargs)
            logger.info("finance_balance_sheet completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in finance_balance_sheet: {e}")
            raise

    def finance_cash_flow(self, *args: Any, **kwargs: Any) -> Any:
        """Get cash flow data.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for finance_cash_flow")
            finance = vnstock.Finance(source=source, symbol=symbol)
            result = finance.cash_flow(*args, **kwargs)
            logger.info("finance_cash_flow completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in finance_cash_flow: {e}")
            raise

    def finance_history(self, *args: Any, **kwargs: Any) -> Any:
        """Get finance history.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for finance_history")
            finance = vnstock.Finance(source=source, symbol=symbol)
            result = finance.history(*args, **kwargs)
            logger.info("finance_history completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in finance_history: {e}")
            raise

    def finance_income_statement(self, *args: Any, **kwargs: Any) -> Any:
        """Get income statement data.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for finance_income_statement")
            finance = vnstock.Finance(source=source, symbol=symbol)
            result = finance.income_statement(*args, **kwargs)
            logger.info("finance_income_statement completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in finance_income_statement: {e}")
            raise

    def finance_ratio(self, *args: Any, **kwargs: Any) -> Any:
        """Get financial ratios.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for finance_ratio")
            finance = vnstock.Finance(source=source, symbol=symbol)
            result = finance.ratio(*args, **kwargs)
            logger.info("finance_ratio completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in finance_ratio: {e}")
            raise

    # =========================================================================
    # COMPANY METHODS (8 methods)
    # =========================================================================

    def company_affiliate(self, *args: Any, **kwargs: Any) -> Any:
        """Get company affiliates.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for company_affiliate")
            company = vnstock.Company(source=source, symbol=symbol)
            result = company.affiliate(*args, **kwargs)
            logger.info("company_affiliate completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in company_affiliate: {e}")
            raise

    def company_events(self, *args: Any, **kwargs: Any) -> Any:
        """Get company events.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for company_events")
            company = vnstock.Company(source=source, symbol=symbol)
            result = company.events(*args, **kwargs)
            logger.info("company_events completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in company_events: {e}")
            raise

    def company_history(self, *args: Any, **kwargs: Any) -> Any:
        """Get company history.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for company_history")
            company = vnstock.Company(source=source, symbol=symbol)
            result = company.history(*args, **kwargs)
            logger.info("company_history completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in company_history: {e}")
            raise

    def company_news(self, *args: Any, **kwargs: Any) -> Any:
        """Get company news.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for company_news")
            company = vnstock.Company(source=source, symbol=symbol)
            result = company.news(*args, **kwargs)
            logger.info("company_news completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in company_news: {e}")
            raise

    def company_officers(self, *args: Any, **kwargs: Any) -> Any:
        """Get company officers.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for company_officers")
            company = vnstock.Company(source=source, symbol=symbol)
            result = company.officers(*args, **kwargs)
            logger.info("company_officers completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in company_officers: {e}")
            raise

    def company_overview(self, *args: Any, **kwargs: Any) -> Any:
        """Get company overview.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for company_overview")
            company = vnstock.Company(source=source, symbol=symbol)
            result = company.overview(*args, **kwargs)
            logger.info("company_overview completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in company_overview: {e}")
            raise

    def company_shareholders(self, *args: Any, **kwargs: Any) -> Any:
        """Get company shareholders.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for company_shareholders")
            company = vnstock.Company(source=source, symbol=symbol)
            result = company.shareholders(*args, **kwargs)
            logger.info("company_shareholders completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in company_shareholders: {e}")
            raise

    def company_subsidiaries(self, *args: Any, **kwargs: Any) -> Any:
        """Get company subsidiaries.

        Args:
            *args: Positional arguments to pass to vnstock.
            **kwargs: Additional arguments to pass to vnstock.

        Returns:
            DataFrame or data from vnstock.
        """
        try:
            source = kwargs.pop("source", "vci")
            symbol = kwargs.pop("symbol", None)
            if not symbol:
                raise ValueError("symbol parameter is required for company_subsidiaries")
            company = vnstock.Company(source=source, symbol=symbol)
            result = company.subsidiaries(*args, **kwargs)
            logger.info("company_subsidiaries completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in company_subsidiaries: {e}")
            raise

    # =========================================================================
    # FUND METHODS (7 methods)
    # =========================================================================

    def fund_asset_holding(self, fund_id: int = 23) -> pd.DataFrame:
        """Get fund asset holdings.

        Args:
            fund_id: Fund ID (default: 23).

        Returns:
            DataFrame with asset holding data.
        """
        try:
            result = self.fund.asset_holding(fundId=fund_id)
            logger.info(f"fund_asset_holding completed for fund: {fund_id}")
            return result
        except Exception as e:
            logger.error(f"Error in fund_asset_holding: {e}")
            raise

    def fund_filter(self, symbol: str = "") -> pd.DataFrame:
        """Filter funds by symbol.

        Args:
            symbol: Fund symbol (optional).

        Returns:
            DataFrame with filtered fund data.
        """
        try:
            result = self.fund.filter(symbol=symbol)
            logger.info(f"fund_filter completed for symbol: {symbol}")
            return result
        except Exception as e:
            logger.error(f"Error in fund_filter: {e}")
            raise

    def fund_industry_holding(self, fund_id: int = 23) -> pd.DataFrame:
        """Get fund industry holdings.

        Args:
            fund_id: Fund ID (default: 23).

        Returns:
            DataFrame with industry holding data.
        """
        try:
            result = self.fund.industry_holding(fundId=fund_id)
            logger.info(f"fund_industry_holding completed for fund: {fund_id}")
            return result
        except Exception as e:
            logger.error(f"Error in fund_industry_holding: {e}")
            raise

    def fund_listing(self, fund_type: str = "") -> pd.DataFrame:
        """Get fund listings.

        Args:
            fund_type: Fund type (optional).

        Returns:
            DataFrame with fund listing data.
        """
        try:
            result = self.fund.listing(fund_type=fund_type)
            logger.info(f"fund_listing completed for fund_type: {fund_type}")
            return result
        except Exception as e:
            logger.error(f"Error in fund_listing: {e}")
            raise

    def fund_nav_report(self, fund_id: int = 23) -> pd.DataFrame:
        """Get fund NAV report.

        Args:
            fund_id: Fund ID (default: 23).

        Returns:
            DataFrame with NAV report data.
        """
        try:
            result = self.fund.nav_report(fundId=fund_id)
            logger.info(f"fund_nav_report completed for fund: {fund_id}")
            return result
        except Exception as e:
            logger.error(f"Error in fund_nav_report: {e}")
            raise

    def fund_top_holding(self, fund_id: int = 23) -> pd.DataFrame:
        """Get fund top holdings.

        Args:
            fund_id: Fund ID (default: 23).

        Returns:
            DataFrame with top holding data.
        """
        try:
            result = self.fund.top_holding(fundId=fund_id)
            logger.info(f"fund_top_holding completed for fund: {fund_id}")
            return result
        except Exception as e:
            logger.error(f"Error in fund_top_holding: {e}")
            raise

    # =========================================================================
    # SCREENER METHODS (1 method)
    # =========================================================================

    def screener_stock(
        self, params: Optional[dict] = None, limit: int = 50, id: Optional[str] = None, lang: str = "vi"
    ) -> pd.DataFrame:
        """Screen stocks based on parameters.

        Args:
            params: Filter parameters dictionary.
            limit: Maximum number of results (default: 50).
            id: Screener ID (optional).
            lang: Language (default: 'vi').

        Returns:
            DataFrame with screened stock data.
        """
        try:
            result = self.screener.stock(params=params, limit=limit, id=id, lang=lang)
            logger.info("screener_stock completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in screener_stock: {e}")
            raise

    # =========================================================================
    # VNSTOCK ROOT METHODS (5 methods)
    # =========================================================================

    def vnstock_stock(self, symbol: Optional[str] = None, source: Optional[str] = None) -> Any:
        """Get stock components.

        Args:
            symbol: Stock symbol.
            source: Data source.

        Returns:
            Stock components object from vnstock.
        """
        try:
            result = self.vnstock_root.stock(symbol=symbol, source=source)
            logger.info(f"vnstock_stock completed for symbol: {symbol}")
            return result
        except Exception as e:
            logger.error(f"Error in vnstock_stock: {e}")
            raise

    def vnstock_fund(self, source: str = "FMARKET") -> Any:
        """Get fund components.

        Args:
            source: Data source (default: 'FMARKET').

        Returns:
            Fund components object from vnstock.
        """
        try:
            result = self.vnstock_root.fund(source=source)
            logger.info("vnstock_fund completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in vnstock_fund: {e}")
            raise

    def vnstock_crypto(self, symbol: Optional[str] = "BTC", source: Optional[str] = "MSN") -> Any:
        """Get crypto components.

        Args:
            symbol: Crypto symbol (default: 'BTC').
            source: Data source (default: 'MSN').

        Returns:
            Crypto components object from vnstock.
        """
        try:
            result = self.vnstock_root.crypto(symbol=symbol, source=source)
            logger.info(f"vnstock_crypto completed for symbol: {symbol}")
            return result
        except Exception as e:
            logger.error(f"Error in vnstock_crypto: {e}")
            raise

    def vnstock_fx(self, symbol: Optional[str] = "EURUSD", source: Optional[str] = "MSN") -> Any:
        """Get forex components.

        Args:
            symbol: Forex symbol (default: 'EURUSD').
            source: Data source (default: 'MSN').

        Returns:
            Forex components object from vnstock.
        """
        try:
            result = self.vnstock_root.fx(symbol=symbol, source=source)
            logger.info(f"vnstock_fx completed for symbol: {symbol}")
            return result
        except Exception as e:
            logger.error(f"Error in vnstock_fx: {e}")
            raise

    def vnstock_world_index(self, symbol: Optional[str] = "DJI", source: Optional[str] = "MSN") -> Any:
        """Get world index components.

        Args:
            symbol: Index symbol (default: 'DJI').
            source: Data source (default: 'MSN').

        Returns:
            World index components object from vnstock.
        """
        try:
            result = self.vnstock_root.world_index(symbol=symbol, source=source)
            logger.info(f"vnstock_world_index completed for symbol: {symbol}")
            return result
        except Exception as e:
            logger.error(f"Error in vnstock_world_index: {e}")
            raise


# Singleton instance
_adapter_instance: Optional[VNStockAdapter] = None


def get_vnstock_adapter() -> VNStockAdapter:
    """Get or create the VNStock adapter singleton.

    Returns:
        VNStockAdapter instance.
    """
    global _adapter_instance
    if _adapter_instance is None:
        _adapter_instance = VNStockAdapter()
    return _adapter_instance
