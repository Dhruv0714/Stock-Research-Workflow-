from crewai import Task
from ..agents.news_agent import news_agent


get_news_sentiment = Task(
    description=(
        "Research recent news and sentiment for the stock: {stock}. Use the company news tool to "
        "retrieve recent headlines and summaries. Classify the overall sentiment as bullish, bearish, "
        "or neutral, and explain the key drivers behind that read."
    ),
    expected_output=(
        "A clear, bullet-pointed summary of:\n"
        "- 2-3 key recent headlines with dates\n"
        "- Overall sentiment label (Bullish / Bearish / Neutral)\n"
        "- Brief justification for the sentiment call"
    ),
    agent=news_agent
)