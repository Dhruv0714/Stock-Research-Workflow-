from crewai import Task
from ..agents.technical_agent import technical_agent


get_technical_analysis = Task(
    description=(
        "Perform technical analysis on the stock: {stock}. Use the historical prices and technical "
        "indicators tools to retrieve moving averages, RSI, MACD, 52-week high/low, and volume trend. "
        "Identify the current trend direction, momentum, and any overbought/oversold signals."
    ),
    expected_output=(
        "A clear, bullet-pointed summary of:\n"
        "- Trend direction (uptrend/downtrend/sideways)\n"
        "- RSI and MACD readings with interpretation\n"
        "- Key support/resistance or 52-week levels\n"
        "- A one-line takeaway on momentum"
    ),
    agent=technical_agent
)