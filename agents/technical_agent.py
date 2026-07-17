import os

from crewai import Agent, LLM
from tools.technical_research_tools import get_historical_prices, get_technical_indicators

my_llm = LLM(
    model=os.environ["GEMINI_API_MODEL"],
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0
)

technical_agent = Agent(
    role="Technical Analysis Specialist",
    goal=(
        "Analyze price action and trading indicators (moving averages, RSI, MACD, 52-week "
        "high/low, volume trends) to identify momentum, trend direction, and potential support "
        "or resistance levels for a given stock."
    ),
    backstory=(
        "You are a chartist who has spent a career reading candlesticks and indicator crossovers "
        "for institutional trading desks. You translate raw indicator values into a clear read on "
        "whether a stock is in an uptrend, downtrend, overbought, or oversold, and you flag "
        "conflicting signals rather than papering over them."
    ),
    llm=my_llm,
    tools=[get_historical_prices, get_technical_indicators],
    verbose=True
)