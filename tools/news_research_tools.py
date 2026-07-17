from crewai.tools import tool
import yfinance as yf
import os
import requests

@tool("Get Company News")
def get_company_news(ticker: str, limit: int = 8) -> str:
    """Fetch recent news headlines and summaries for a ticker to support sentiment analysis."""
    news_items = yf.Ticker(ticker).news[:limit]
    if not news_items:
        return f"No recent news found for {ticker}."
 
    lines = []
    for item in news_items:
        content = item.get("content", item)
        title = content.get("title", "Untitled")
        publisher = content.get("provider", {}).get("displayName", "Unknown")
        pub_date = content.get("pubDate", "")
        lines.append(f"- [{pub_date}] ({publisher}) {title}")
    return "\n".join(lines)

SERPER_URL = "https://google.serper.dev/search"

@tool("Search News Context")
def search_news_context(headline: str) -> str:
    """Search the web for a given news headline to pull full context, source, and related coverage."""
    headers = {"X-API-KEY": os.environ["SERPER_API_KEY"], "Content-Type": "application/json"}
    payload = {"q": headline, "tbm": "nws", "num": 5}
    resp = requests.post(SERPER_URL, headers=headers, json=payload, timeout=10)
    resp.raise_for_status()
    results = resp.json().get("news", [])

    if not results:
        return f"No additional context found for: {headline}"

    lines = [f"- {r.get('title')} ({r.get('source')}, {r.get('date')}): {r.get('snippet')}" for r in results]
    return "\n".join(lines)