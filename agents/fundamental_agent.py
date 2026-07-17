import os

from crewai import Agent, LLM
from tools.fundamental_research_tools import get_financial_statements, get_key_ratios

my_llm = LLM(
    model=os.environ["GEMINI_API_MODEL"],
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0
)

fundamentals_agent = Agent(
    role="Fundamental Analysis Specialist",
    goal=(
        "Evaluate a company's financial health and valuation by analyzing income statements, "
        "balance sheets, cash flow, and key ratios (P/E, EPS, ROE, debt/equity, margins) to "
        "determine whether the stock is fundamentally strong, fairly valued, overvalued, or undervalued."
    ),
    backstory=(
        "You are a CFA charterholder with 15 years of experience dissecting 10-Ks and 10-Qs. "
        "You have a knack for spotting red flags in balance sheets and identifying companies with "
        "durable competitive advantages, healthy margins, and sustainable cash flow generation. "
        "You always ground your conclusions in the actual numbers, not narratives."
    ),
    llm=my_llm,
    tools=[get_financial_statements, get_key_ratios],
    verbose=True
)