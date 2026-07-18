import os
from getpass import getpass

import yfinance as yf
from dotenv import load_dotenv
from stock_researcher_workflow.crew import stock_crew


def get_key(env_name: str, prompt: str) -> str:
    """
    Resolve an API key in this order:
      1. Already set as a real environment variable
      2. Loaded from a .env file in the current working directory
      3. Prompted interactively (hidden input, not echoed, not stored)
    """
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

    result = stock_crew.kickoff(inputs={"stock": stock})
    print(result)


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