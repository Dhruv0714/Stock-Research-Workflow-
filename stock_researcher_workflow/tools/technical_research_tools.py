import yfinance as yf
import pandas as pd
from crewai.tools import tool


@tool("Get Historical Prices")
def get_historical_prices(ticker: str, period: str = "6mo") -> str:
    """Fetch historical OHLCV price data for a ticker over a given period (e.g. 1mo, 6mo, 1y)."""
    hist = yf.Ticker(ticker).history(period=period)
    if hist.empty:
        return f"No historical data found for {ticker}."
    recent = hist.tail(10)[["Open", "High", "Low", "Close", "Volume"]]
    return recent.to_string()
 
 
@tool("Find Technical Indicators")
def get_technical_indicators(ticker: str, period: str = "6mo") -> str:
    """Compute SMA20/50, RSI(14), and MACD for a ticker to support technical analysis."""
    hist = yf.Ticker(ticker).history(period=period)
    if hist.empty:
        return f"No historical data found for {ticker}."
 
    close = hist["Close"]
 
    sma20 = close.rolling(20).mean().iloc[-1]
    sma50 = close.rolling(50).mean().iloc[-1] if len(close) >= 50 else None
 
    # RSI (14)
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    rsi_latest = rsi.iloc[-1]
 
    # MACD (12, 26, 9)
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
 
    result = {
        "current_price": round(close.iloc[-1], 2),
        "sma20": round(sma20, 2) if pd.notna(sma20) else None,
        "sma50": round(sma50, 2) if sma50 is not None and pd.notna(sma50) else None,
        "rsi14": round(rsi_latest, 2) if pd.notna(rsi_latest) else None,
        "macd": round(macd_line.iloc[-1], 3),
        "macd_signal": round(signal_line.iloc[-1], 3),
        "52w_high": round(hist["High"].max(), 2),
        "52w_low": round(hist["Low"].min(), 2),
    }
    return str(result)
