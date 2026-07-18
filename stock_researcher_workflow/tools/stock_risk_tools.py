import yfinance as yf
from crewai.tools import tool
import pandas as pd

@tool("Calculate Beta And Volatility")
def calculate_beta_volatility(ticker: str, benchmark: str = "^GSPC", period: str = "1y") -> str:
    """Calculate beta vs a benchmark index, annualized volatility, and max drawdown for a ticker."""
    stock_hist = yf.Ticker(ticker).history(period=period)["Close"]
    bench_hist = yf.Ticker(benchmark).history(period=period)["Close"]
 
    if stock_hist.empty or bench_hist.empty:
        return f"Insufficient data to calculate risk metrics for {ticker}."
 
    stock_returns = stock_hist.pct_change().dropna()
    bench_returns = bench_hist.pct_change().dropna()
 
    aligned = pd.concat([stock_returns, bench_returns], axis=1, join="inner")
    aligned.columns = ["stock", "bench"]
 
    covariance = aligned["stock"].cov(aligned["bench"])
    variance = aligned["bench"].var()
    beta = covariance / variance if variance != 0 else None
 
    annualized_vol = stock_returns.std() * (252 ** 0.5)
 
    cumulative = (1 + stock_returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max
    max_drawdown = drawdown.min()
 
    result = {
        "beta_vs_benchmark": round(beta, 3) if beta is not None else None,
        "annualized_volatility": round(annualized_vol, 3),
        "max_drawdown": round(max_drawdown, 3),
        "benchmark": benchmark,
    }
    return str(result)

@tool("Get the Historical Prices")
def get_historical_prices(ticker: str, period: str = "6mo") -> str:
    """Fetch historical OHLCV price data for a ticker over a given period (e.g. 1mo, 6mo, 1y)."""
    hist = yf.Ticker(ticker).history(period=period)
    if hist.empty:
        return f"No historical data found for {ticker}."
    recent = hist.tail(10)[["Open", "High", "Low", "Close", "Volume"]]
    return recent.to_string()
 