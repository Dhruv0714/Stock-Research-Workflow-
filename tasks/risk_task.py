from crewai import Task
from agents.risk_agent import risk_agent


get_risk_assessment = Task(
    description=(
        "Assess the risk profile of the stock: {stock}. Use the beta/volatility calculation and "
        "historical prices tools to determine beta versus the S&P 500 benchmark, annualized "
        "volatility, and maximum drawdown over the past year."
    ),
    expected_output=(
        "A clear, bullet-pointed summary of:\n"
        "- Beta relative to the S&P 500\n"
        "- Annualized volatility\n"
        "- Maximum drawdown over the past year\n"
        "- A one-line takeaway on overall risk level"
    ),
    agent=risk_agent
)