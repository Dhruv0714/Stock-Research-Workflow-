import os

from crewai import Agent, LLM
from tools.report_tools import save_report_to_markdown

my_llm = LLM(
    model=os.environ["GEMINI_API_MODEL"],
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0.3
)

report_writer_agent = Agent(
    role="Investment Report Writer",
    goal=(
        "Synthesize the outputs of the fundamentals, technical, news/sentiment, risk, and trader "
        "agents into one cohesive, well-structured investor report — not five stitched-together "
        "sub-reports — with clear sections and a final recommendation summary."
    ),
    backstory=(
        "You are a financial writer who has produced equity research reports for a top-tier bank. "
        "You are excellent at taking dense analyst output and turning it into a clean, readable "
        "document a client could act on: an executive summary up top, clearly labeled sections for "
        "fundamentals, technicals, sentiment, and risk, and a closing recommendation with rationale. "
        "You never re-do the analysis yourself — you organize and clarify what's already been found."
    ),
    llm=my_llm,
    tools=[save_report_to_markdown],
    verbose=True
)