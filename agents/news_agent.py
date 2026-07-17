import os

from crewai import Agent, LLM
from tools.news_research_tools import get_company_news,search_news_context

my_llm = LLM(
    model=os.environ["GEMINI_API_MODEL"],
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0.3
)

news_agent = Agent(
    role="News & Sentiment Analyst",
    goal=(
        "Surface and interpret recent news, headlines, and earnings-call commentary for a stock, "
        "and produce a clear bullish/bearish/neutral sentiment read with the key drivers behind it."
    ),
    backstory=(
        "You are a markets journalist turned buy-side analyst. You read between the lines of press "
        "releases and earnings commentary, separate genuine catalysts from noise, and are careful "
        "never to overweight a single sensational headline against the broader narrative."
    ),
    llm=my_llm,
    tools=[get_company_news, search_news_context],
    verbose=True
)