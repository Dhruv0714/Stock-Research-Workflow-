import os
from datetime import datetime, timezone

import requests
import yfinance as yf
from crewai.tools import tool

SERPER_URL = "https://google.serper.dev/search"


@tool("Get Company News")
def get_company_news(ticker: str, limit: int = 5) -> str:
    """
    Fetch the most recent material news for a company.

    Returns at most the latest 5 news articles sorted by publication date.
    """
    try:
        news = yf.Ticker(ticker).news

        if not news:
            return f"No recent news found for {ticker}."

        parsed_news = []
        for item in news:
            content = item.get("content", item)
            title = content.get("title", "Untitled")
            publisher = content.get("provider", {}).get("displayName", "Unknown")
            pub_date = content.get("pubDate", "")
            url = (
                content.get("canonicalUrl", {}).get("url")
                or content.get("clickThroughUrl", {}).get("url")
                or "No URL Available"
            )

            try:
                dt = datetime.fromisoformat(pub_date.replace("Z", "+00:00"))
            except Exception:
                dt = datetime.min.replace(tzinfo=timezone.utc)

            parsed_news.append(
                {
                    "date": dt,
                    "title": title,
                    "publisher": publisher,
                    "url": url,
                }
            )

        parsed_news.sort(key=lambda x: x["date"], reverse=True)
        parsed_news = parsed_news[:limit]

        lines = []
        for i, item in enumerate(parsed_news, 1):
            lines.append(f"""
### {i}. {item['title']}

- **Date:** {item['date'].strftime('%Y-%m-%d')}
- **Source:** {item['publisher']}
- **URL:** {item['url']}
""")

        return "\n".join(lines)

    except Exception as e:
        return f"Error retrieving news: {str(e)}"


@tool("Search News Context")
def search_news_context(headline: str) -> str:
    """
    Search multiple news sources for detailed context about a headline.
    """
    headers = {
        "X-API-KEY": os.environ["SERPER_API_KEY"],
        "Content-Type": "application/json",
    }
    payload = {
        "q": headline,
        "tbm": "nws",
        "num": 5,
    }

    try:
        response = requests.post(SERPER_URL, headers=headers, json=payload, timeout=20)
        response.raise_for_status()

        news = response.json().get("news", [])
        if not news:
            return f"No additional context found for: {headline}"

        lines = []
        for i, article in enumerate(news, 1):
            lines.append(f"""
### Source {i}

**Title:** {article.get("title")}

**Source:** {article.get("source")}

**Date:** {article.get("date")}

**Summary:**
{article.get("snippet")}

**URL:**
{article.get("link")}
""")

        return "\n".join(lines)

    except Exception as e:
        return f"Error searching news context: {str(e)}"



@tool("Search Company History")
def search_company_history(company: str) -> str:
    """
    Search for the most important historical corporate events
    that remain relevant for investors today.
    """
    headers = {
        "X-API-KEY": os.environ["SERPER_API_KEY"],
        "Content-Type": "application/json",
    }
    query = (
        f"{company} major historical events acquisitions "
        f"CEO changes lawsuits partnerships product launches "
        f"important company history investors"
    )
    payload = {
        "q": query,
        "num": 5,
    }

    try:
        response = requests.post(SERPER_URL, headers=headers, json=payload, timeout=20)
        response.raise_for_status()

        results = response.json().get("organic", [])
        if not results:
            return f"No historical company information found for {company}."

        lines = []
        for i, result in enumerate(results[:5], 1):
            lines.append(f"""
        ### Historical Event {i}

        **Title:** {result.get("title")}

        **Summary:**
        {result.get("snippet")}

        **URL:**
        {result.get("link")}
        """)

        return "\n".join(lines)

    except Exception as e:
        return f"Error searching company history: {str(e)}"
