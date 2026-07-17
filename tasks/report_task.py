from crewai import Task
from agents.report_writer_agent import report_writer_agent

from tasks.analyse_task import get_stock_analysis
from tasks.fundamental_task import get_fundamentals_analysis
from tasks.technical_task import get_technical_analysis
from tasks.news_task import get_news_sentiment
from tasks.risk_task import get_risk_assessment
from tasks.trade_task import trade_decision


compile_final_report = Task(
    description=(
        "Compile all prior analysis into one polished, well-structured investor report for {stock} "
        "with sections: Executive Summary, Market Snapshot, Fundamentals, Technicals, Sentiment, "
        "Risk, and Recommendation. Save the report using the markdown save tool."
    ),
    expected_output=(
        "A complete markdown investor report covering every section, saved to disk via the save tool, "
        "and also returned as the task's final text output."
    ),
    agent=report_writer_agent,
    context=[get_stock_analysis, get_fundamentals_analysis, get_technical_analysis, get_news_sentiment, get_risk_assessment, trade_decision]
)