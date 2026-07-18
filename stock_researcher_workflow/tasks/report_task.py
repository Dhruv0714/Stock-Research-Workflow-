from crewai import Task
from ..agents.report_writer_agent import report_writer_agent

from .analyse_task import get_stock_analysis
from .fundamental_task import get_fundamentals_analysis
from .technical_task import get_technical_analysis
from .news_task import get_news_sentiment
from .risk_task import get_risk_assessment
from .trade_task import trade_decision


compile_final_report = Task(
    description=(
        "Compile all prior analysis into one polished, well-structured detailed investor report for {stock} "
        "with sections: Executive Detailed analysis, Market Snapshot Analysis, Fundamentals Analysis, Technicals Analysis, Sentiment with Analysis, "
        "Risk Analysis, and Recommendation. Save the report using the markdown save tool."
    ),
    expected_output=(
        "A complete markdown investor report covering every section, saved to disk via the save tool, "
        "and also returned as the task's final text output."
        "It should innclude all the references/links used by the agents in their analysis, and a final recommendation summary."
        "It should be a 150+ lines detailed report"
    ),
    agent=report_writer_agent,
    context=[get_stock_analysis, get_fundamentals_analysis, get_technical_analysis, get_news_sentiment, get_risk_assessment, trade_decision]
)