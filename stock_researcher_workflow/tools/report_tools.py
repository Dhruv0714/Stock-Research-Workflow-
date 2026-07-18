import os
from crewai.tools import tool


@tool("Save Report To Markdown")
def save_report_to_markdown(ticker: str, report_content: str) -> str:
    """Save the final compiled stock report as a markdown file named after the ticker."""
    os.makedirs("reports", exist_ok=True)
    filepath = f"reports/{ticker.upper()}_report.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_content)
    return f"Report saved to {filepath}"