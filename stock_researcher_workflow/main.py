import sys
import io
import logging

from dotenv import load_dotenv
import yfinance as yf
from rich.panel import Panel

from crew import build_crew, TASK_LABELS
from console_ui import WorkflowDashboard, console

load_dotenv()

# Quiet third-party libs that print outside Rich's control
logging.getLogger("LiteLLM").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.WARNING)


def is_valid_stock(symbol: str):
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


if __name__ == "__main__":

    while True:
        stock = input("Enter stock ticker (e.g. AAPL, TSLA, NVDA): ").strip().upper()

        if is_valid_stock(stock):
            break

        print(f"\n'{stock}' is not a valid stock ticker. Please try again.\n")

    run(stock)
