from crewai import Crew, Process
from .agents.fundamental_agent import fundamentals_agent
from .agents.analyst_agent import analyst_agent
from .agents.technical_agent import technical_agent
from .agents.news_agent import news_agent
from .agents.risk_agent import risk_agent
from .agents.trader_agent import trader_agent
from .agents.report_writer_agent import report_writer_agent

from .tasks.analyse_task import get_stock_analysis
from .tasks.fundamental_task import get_fundamentals_analysis
from .tasks.technical_task import get_technical_analysis
from .tasks.news_task import get_news_sentiment
from .tasks.risk_task import get_risk_assessment
from .tasks.trade_task import trade_decision
from .tasks.report_task import compile_final_report

TASK_LABELS = [
    "Market Snapshot",
    "Fundamental Analysis",
    "Technical Analysis",
    "News & Sentiment",
    "Risk Assessment",
    "Investment Decision",
    "Final Report",
]

# (task_object, label, next_label) — mirrors execution order
_TASK_CHAIN = [
    (get_stock_analysis, "Market Snapshot", "Fundamental Analysis"),
    (get_fundamentals_analysis, "Fundamental Analysis", "Technical Analysis"),
    (get_technical_analysis, "Technical Analysis", "News & Sentiment"),
    (get_news_sentiment, "News & Sentiment", "Risk Assessment"),
    (get_risk_assessment, "Risk Assessment", "Investment Decision"),
    (trade_decision, "Investment Decision", "Final Report"),
    (compile_final_report, "Final Report", None),
]


def build_crew(dashboard) -> Crew:
    """Attach dashboard callbacks to each task, then assemble the Crew."""
    for task_obj, label, next_label in _TASK_CHAIN:
        task_obj.callback = _make_callback(dashboard, label, next_label)

    return Crew(
        agents=[
            analyst_agent,
            fundamentals_agent,
            technical_agent,
            news_agent,
            risk_agent,
            trader_agent,
            report_writer_agent,
        ],
        tasks=[t for t, _, _ in _TASK_CHAIN],
        process=Process.sequential,
        verbose=False,
    )


def _make_callback(dashboard, label, next_label):
    def _callback(output):
        dashboard.complete_task(label, next_label)

    return _callback
