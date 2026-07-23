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
        "Your ONLY responsibility is to assemble the outputs received from the context tasks into a single, "
        "well-formatted markdown report.\n\n"

        "Do NOT perform any additional financial analysis.\n"
        "Do NOT summarize, shorten, reinterpret, or remove information.\n"
        "Do NOT generate new insights or recommendations beyond what already exists in the provided outputs.\n"
        "Do NOT omit tables, bullet points, metrics, references, URLs, or citations provided by previous agents.\n\n"

        "Use each context output as the content for its corresponding section.\n\n"

        "Create the report in the following order:\n"
        "# {stock} Investment Research Report\n\n"
        "## Executive Summary\n"
        "(Insert ONLY the output from the Trade Decision agent.)\n\n"
        "## Market Snapshot Analysis\n"
        "(Insert the complete output from the Stock Analysis agent.)\n\n"
        "## Fundamentals Analysis\n"
        "(Insert the complete output from the Fundamentals agent.)\n\n"
        "## Technical Analysis\n"
        "(Insert the complete output from the Technical Analysis agent.)\n\n"
        "## News & Sentiment Analysis\n"
        "(Insert the complete output from the News Sentiment agent.)\n\n"
        "## Risk Analysis\n"
        "(Insert the complete output from the Risk Assessment agent.)\n\n"
        "## Final Recommendation\n"
        "(Insert the complete output from the Trade Decision agent exactly as provided.)\n\n"

        "After all sections, create a final section titled:\n"
        "## References\n"
        "Collect every URL, citation, report link, SEC filing, news article, earnings report, "
        "or external reference mentioned anywhere in the previous outputs. "
        "Remove duplicate links while preserving all unique references.\n\n"

        "Preserve all formatting from the original outputs whenever possible, including:\n"
        "- Tables\n"
        "- Markdown headings\n"
        "- Lists\n"
        "- Code blocks (if any)\n"
        "- Images/links\n"
        "- Numerical values\n\n"

        "Finally, save the complete markdown document using the markdown save tool."
    ),
    expected_output=(
        "A single markdown document that is simply the concatenation of the outputs from all previous agents "
        "organized into the specified sections. No additional analysis, summarization, rewriting, or content generation "
        "should be performed. The report should preserve the original detail and formatting, include all references, "
        "and be saved to disk using the markdown save tool while also being returned as the final task output."
    ),
    agent=report_writer_agent,
    context=[
        get_stock_analysis,
        get_fundamentals_analysis,
        get_technical_analysis,
        get_news_sentiment,
        get_risk_assessment,
        trade_decision,
    ],
)