from crewai import Task
from ..agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description=(f"""
      Analyze the publicly traded company: {{stock}}.

      Use the available market data tools to retrieve the latest trading information and prepare a professional
      Market Snapshot report.

      Focus ONLY on describing the company's current market performance.
      Do NOT perform: ̰
   - Fundamental analysis
   - Technical indicator analysis
   - News or sentiment analysis
   - Risk assessment
   - Buy/Hold/Sell recommendation
    ̰
   Your analysis should include:

   1. Company Information
      - Company Name
      - Ticker
      - Exchange
      - Sector
      - Industry

   2. Current Trading Statistics
      - Current Price
   - Previous Close
   - Open
   - Day High
   - Day Low
   - 52 Week High
   - 52 Week Low
   - Market Cap
   - Trading Volume

3. Market Performance
   - Daily Price Change
   - Percentage Change
   - Volume Analysis
   - Liquidity observations

4. Market Observations
   - Significant price movement
   - Unusual trading activity
   - Market behavior
   - Any notable observations supported by data

For every metric:
- Explain what it represents.
- Explain why it matters.
- Interpret the current value.

If data is unavailable, explicitly mention it.
Never fabricate values.
Use Markdown headings, tables and bullet points.
"""),
    expected_output=("""
A detailed professional Market Snapshot report in Markdown.

The report should contain:
- Well-structured headings
- Tables for numerical data
- Bullet points for observations
- Interpretation of every important metric
- 5–10 key takeaways

The report should be approximately 700–1200 words.
No investment recommendation should be included.
"""),
    agent=analyst_agent,
)
