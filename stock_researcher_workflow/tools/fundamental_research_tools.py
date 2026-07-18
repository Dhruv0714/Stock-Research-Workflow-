import yfinance as yf
import pandas as pd
from crewai.tools import tool

@tool("Get Financial Statements")
def get_financial_statements(ticker: str) -> str:
    """Fetch a summary of income statement, balance sheet, and cash flow for a ticker."""
    stock = yf.Ticker(ticker)
    income = stock.financials
    balance = stock.balance_sheet
    cashflow = stock.cashflow
 
    def latest_col(df, rows):
        if df is None or df.empty:
            return {}
        col = df.columns[0]
        out = {}
        for r in rows:
            if r in df.index:
                out[r] = df.loc[r, col]
        return out
 
    summary = {
        "income_statement": latest_col(income, ["Total Revenue", "Gross Profit", "Net Income", "EBITDA"]),
        "balance_sheet": latest_col(balance, ["Total Assets", "Total Liabilities Net Minority Interest", "Total Debt", "Cash And Cash Equivalents"]),
        "cash_flow": latest_col(cashflow, ["Free Cash Flow", "Operating Cash Flow", "Capital Expenditure"]),
    }
    return str(summary)

@tool("Get Key Ratios")
def get_key_ratios(ticker: str) -> str:
    """Fetch key valuation and profitability ratios: P/E, EPS, ROE, debt/equity, margins."""
    info = yf.Ticker(ticker).info
    ratios = {
        "trailing_pe": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "eps_trailing": info.get("trailingEps"),
        "eps_forward": info.get("forwardEps"),
        "price_to_book": info.get("priceToBook"),
        "return_on_equity": info.get("returnOnEquity"),
        "debt_to_equity": info.get("debtToEquity"),
        "profit_margin": info.get("profitMargins"),
        "revenue_growth": info.get("revenueGrowth"),
        "market_cap": info.get("marketCap"),
    }
    return str(ratios)

 