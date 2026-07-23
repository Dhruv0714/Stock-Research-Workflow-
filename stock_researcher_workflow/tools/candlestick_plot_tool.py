import matplotlib
matplotlib.use("Agg")  
from crewai.tools import tool
import yfinance as yf
import mplfinance as mpf
import os
from crewai import LLM
import base64

vision_llm = LLM(
    model=os.environ["GEMINI_API_MODEL"],
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0
)

@tool("Generate Price Chart")
def generate_price_chart(ticker: str, period: str = "6mo") -> str:
    """Generate a candlestick chart with SMA20/50 overlay and volume, saved as PNG."""
    df = yf.Ticker(ticker).history(period=period)
    os.makedirs("reports/charts", exist_ok=True)
    path = f"reports/charts/{ticker}_chart.png"

    mpf.plot(
        df,
        type="candle",
        mav=(20, 50),
        volume=True,
        style="yahoo",
        savefig=path,
        title=f"{ticker} — Price, MAs, Volume ({period})",
    )
    return f"Chart saved to {path}"

@tool("Analyze Chart Image")
def analyze_chart_image(image_path: str) -> str:
    """Visually inspect a saved candlestick chart PNG and describe trend, patterns, and support/resistance levels seen in the image."""
    with open(image_path, "rb") as f:
        b64_image = base64.b64encode(f.read()).decode("utf-8")

    response = vision_llm.call(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "You are a technical analyst. Examine this candlestick chart. "
                            "Describe: overall trend direction, any visible candlestick patterns "
                            "(doji, hammer, engulfing, etc.), support/resistance levels, and volume behavior."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{b64_image}"},
                    },
                ],
            }
        ]
    )
    return response