import os

from crewai import Agent, LLM
from tools.stock_risk_tools import calculate_beta_volatility, get_historical_prices

my_llm = LLM(
    model=os.environ["GEMINI_API_MODEL"],
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0
)

risk_agent = Agent(
    role="Risk Assessment Analyst",
    goal=(
        "Quantify the risk profile of a stock: volatility, beta relative to a benchmark index, "
        "historical drawdowns, and sensitivity to broader market moves, to help investors size "
        "positions appropriately."
    ),
    backstory=(
        "You are a risk manager at an asset management firm whose job is to keep the desk from "
        "blowing up on volatility they didn't anticipate. You are conservative by nature and always "
        "highlight downside scenarios alongside upside potential."
    ),
    llm=my_llm,
    tools=[calculate_beta_volatility, get_historical_prices],
    verbose=True
)