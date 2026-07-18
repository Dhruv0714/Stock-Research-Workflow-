from crewai import Task
from ..agents.trader_agent import trader_agent

from .analyse_task import get_stock_analysis
from .fundamental_task import get_fundamentals_analysis
from .technical_task import get_technical_analysis
from .news_task import get_news_sentiment
from .risk_task import get_risk_assessment


trade_decision = Task(
    description=(
        "Using the market snapshot, fundamentals, technical, sentiment, and risk analysis provided "
        "for {stock}, make a strategic trading decision. Weigh current price action, valuation, "
        "momentum, sentiment, and risk against each other, then recommend whether to **Buy**, "
        "**Sell**, or **Hold** the stock."
    ),
    expected_output=(
        "A clear and confident trading recommendation (Buy / Sell / Hold), supported by:\n"
        "- Current stock price and daily change\n"
        "- Fundamental valuation view\n"
        "- Technical/momentum signals\n"
        "- Sentiment and risk considerations\n"
        "- A target price range and justification for the trading action"
    ),
    agent=trader_agent,
    context=[get_stock_analysis, get_fundamentals_analysis, get_technical_analysis, get_news_sentiment, get_risk_assessment]
)