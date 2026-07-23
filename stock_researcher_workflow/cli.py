import os
import sys
import io
import logging
from getpass import getpass

import yfinance as yf
from dotenv import load_dotenv
from rich.panel import Panel

from stock_researcher_workflow.crew import build_crew, TASK_LABELS
from stock_researcher_workflow.console_ui import WorkflowDashboard, console

# Quiet third-party libs that print outside Rich's control
logging.getLogger("LiteLLM").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.WARNING)


def get_key(env_name: str, prompt: str) -> str:
    value = os.getenv(env_name)
    if value:
        return value
    return getpass(f"{prompt}: ")


def is_valid_stock(symbol: str) -> bool:
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        return bool(info and info.get("symbol") and info.get("longName"))
    except Exception:
        return False


def run(stock: str):
    dashboard = WorkflowDashboard(stock, TASK_LABELS)
    crew = build_crew(dashboard)

    dashboard.start()
    dashboard.start_task(TASK_LABELS[0])

    result = crew.kickoff(inputs={"stock": stock})  # no stdout redirect for now

    dashboard.stop()
    console.print(
        Panel(str(result), title=f"Final Report · {stock}", border_style="green")
    )


def main():
    load_dotenv()

    gemini_key = get_key("GEMINI_API_KEY", "Enter your Gemini API key")
    serper_key = get_key("SERPER_API_KEY", "Enter your Serper API key")

    if not gemini_key or not serper_key:
        print("Both GEMINI_API_KEY and SERPER_API_KEY are required to run this tool.")
        return

    os.environ["GEMINI_API_KEY"] = gemini_key
    os.environ["SERPER_API_KEY"] = serper_key

    while True:
        stock = input("Enter stock ticker (e.g. AAPL, TSLA, NVDA): ").strip().upper()
        if is_valid_stock(stock):
            break
        print(f"\n'{stock}' is not a valid stock ticker. Please try again.\n")

    run(stock)


if __name__ == "__main__":
    main()
