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

 
stock_crew = Crew(
    agents=[
        analyst_agent,
        fundamentals_agent,
        technical_agent,
        news_agent,
        risk_agent,
        trader_agent,
        report_writer_agent,
    ],
    tasks=[
        get_stock_analysis,
        get_fundamentals_analysis,
        get_technical_analysis,
        get_news_sentiment,
        get_risk_assessment,
        trade_decision,
        compile_final_report,
    ],
    process=Process.sequential,
    verbose=True
)

