from crewai import Task
from ..agents.news_agent import news_agent

get_news_sentiment = Task(
    description=("""
Conduct a comprehensive news and market sentiment analysis for the publicly traded company: {stock}.

Use the available news and research tools to gather the most recent and relevant information about
the company. Focus on material developments that could influence investor sentiment or the company's
future performance.

Your objective is to identify the key catalysts currently driving market sentiment and determine
whether the overall outlook is Bullish, Neutral, or Bearish based on the available evidence.

Focus ONLY on news and sentiment analysis.

Do NOT perform:
- Fundamental analysis
- Technical analysis
- Risk assessment
- Valuation analysis
- Buy/Hold/Sell recommendations

Evaluate each important news item by explaining:
- What happened
- Why it is important
- Its likely impact on investors
- Whether the impact is Positive, Negative, or Neutral

If multiple articles discuss the same event, consolidate them into a single analysis instead of
repeating similar information.

Prioritize high-quality and authoritative sources. Include the publication date and source link
for every significant news item.

Present the report using professional Markdown headings, tables, and bullet points.
"""),
    expected_output=("""
Return a professional Markdown report with the following sections:

# Overall Market Sentiment
- Overall Sentiment (Bullish / Neutral / Bearish)
- Confidence Level
- Summary of the current market narrative

# Major Recent Developments
For each significant news item include:
- Headline
- Publication Date
- Source
- Source URL
- Summary
- Market Impact (Positive / Neutral / Negative)

# Earnings & Corporate Updates
- Earnings announcements
- Guidance changes
- Management commentary
- Strategic initiatives
- Product launches
- Partnerships
- Acquisitions
- Other important corporate developments

# Positive Catalysts
List the major factors supporting positive investor sentiment.

# Negative Catalysts
List the major factors contributing to negative investor sentiment.

# Industry & Macroeconomic Factors
Summarize relevant industry trends, regulatory developments, and macroeconomic events affecting the company.

# Key Sentiment Drivers
Identify and explain the most important factors currently influencing investor sentiment.

# Overall Sentiment Assessment
Provide a balanced conclusion explaining:
- Why the overall sentiment is Bullish, Neutral, or Bearish
- The likely short-term impact
- The likely medium-term impact
- The likely long-term impact

Requirements:
- Use Markdown headings.
- Use tables where appropriate.
- Include publication dates for all news items.
- Include working source URLs for every significant article.
- Avoid duplicate news coverage.
- Clearly distinguish factual reporting from interpretation.
- Do not provide investment recommendations.
"""),
    agent=news_agent,
)
