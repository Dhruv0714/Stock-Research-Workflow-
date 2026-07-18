from crewai import Task
from ..agents.fundamental_agent import fundamentals_agent


get_fundamentals_analysis = Task(
    description=(
        "Analyze the fundamentals of the stock: {stock}. Use the financial statements and key ratios "
        "tools to retrieve revenue, profit, balance sheet health, and valuation ratios (P/E, EPS, ROE, "
        "debt/equity, profit margins). Determine whether the company looks fundamentally strong, fairly "
        "valued, overvalued, or undervalued."
    ),
    expected_output=(
        "A clear, bullet-pointed summary of:\n"
        "- Revenue, profit, and margin trends\n"
        "- Balance sheet health (debt, cash position)\n"
        "- Key valuation ratios (P/E, EPS, ROE)\n"
        "- A detailed takeaway on fundamental strength"
    ),
    agent=fundamentals_agent
)