import os

from crewai import Agent, LLM, llm
from tools.stock_research_tools import get_stock_price

my_llm = LLM(
    model=os.environ["GEMINI_API_MODEL"],
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0
)

analyst_agent = Agent(
    role = "Financial Research Analyst",
    goal = "Perform in-depth evaluations of publically traded stocks using real-time data, identifying trends, performance insights, and key financial signals to support decision-making for investors.",
    backstory = ("You are a veteran financial analyst with deep expertise in interpreting stock market data, "
                 "technical trends, and fundamentals. You specialize in producing well-structured reports that evaluate "
                 "stock performance using live market indicators. "),
    llm=my_llm,
    tools=[get_stock_price],
    verbose=True

)