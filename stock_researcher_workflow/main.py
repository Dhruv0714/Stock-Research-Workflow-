from dotenv import load_dotenv
from crew import stock_crew
import yfinance as yf

load_dotenv()


def is_valid_stock(symbol: str):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        return (
            info
            and info.get("symbol")
            and info.get("longName")
        )
    except Exception:
        return False

def run(stock: str):
    result = stock_crew.kickoff(inputs={"stock": stock})
    print(result)


if __name__ == "__main__":

    while True:
        stock = input(
            "Enter stock ticker (e.g. AAPL, TSLA, NVDA): "
        ).strip().upper()

        if is_valid_stock(stock):
            break

        print(f"\n'{stock}' is not a valid stock ticker. Please try again.\n")

    run(stock)