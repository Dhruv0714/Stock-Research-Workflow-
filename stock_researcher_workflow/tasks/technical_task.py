from crewai import Task
from ..agents.technical_agent import technical_agent


get_technical_analysis = Task(
    description=("""
Conduct a comprehensive technical analysis of the publicly traded company: {stock}.

Follow the workflow below in order:

Step 1:
Retrieve sufficient historical price and volume data.

Step 2:
Calculate all available technical indicators using the technical analysis tools.

Step 3:
Generate a candlestick price chart using the chart generation tool.

Step 4:
Pass the generated chart to the chart image analysis tool to perform a visual inspection of the price action.

Step 5:
Combine the quantitative indicator analysis with the visual chart analysis into one coherent technical report.

Your analysis should focus ONLY on technical analysis.

Do NOT discuss:
- Company fundamentals
- Financial statements
- Valuation
- News or sentiment
- Risk assessment
- Investment recommendations

Evaluate and interpret all available technical indicators.

For every important indicator:
- Report the calculated value.
- Explain what the indicator measures.
- Explain why traders monitor it.
- Interpret whether the reading is Bullish, Bearish, or Neutral.

During the visual chart inspection identify:
- Overall trend
- Market structure
- Candlestick patterns
- Support levels
- Resistance levels
- Breakout or breakdown zones
- Volume confirmation
- Trend strength
- Any visually significant observations

If the chart analysis contradicts the numerical indicators, explicitly explain:
- Which signals disagree.
- Possible reasons for the disagreement.
- Which evidence appears more reliable and why.

Support every conclusion with quantitative or visual evidence.

Present the report using professional Markdown headings, tables, and bullet points.
"""),
    expected_output=("""
Return a professional Markdown report with the following sections.

# Technical Overview
- Overall Trend
- Confidence Level
- Time Horizon

# Price Action
- Recent price movement
- Market structure
- Trend quality

# Trend Indicators
- 20-day Moving Average
- 50-day Moving Average
- 100-day Moving Average (if available)
- 200-day Moving Average
- Trend interpretation

# Momentum Indicators
- RSI
- MACD
- Signal Line
- Histogram
- Interpretation

# Volume Analysis
- Volume trend
- Volume confirmation
- Unusual trading activity

# Support & Resistance
- Major support levels
- Major resistance levels
- Important breakout levels
- Important breakdown levels

# Chart Image Analysis
- Visual observations
- Candlestick patterns
- Trend channels
- Breakout formations
- Reversal patterns
- Volume behaviour
- Market structure

# Indicator vs Chart Comparison
Explain any agreement or disagreement between:
- Indicator calculations
- Visual chart observations

# Technical Outlook
Summarize:
- Bullish evidence
- Bearish evidence
- Neutral evidence
- Overall momentum
- Most probable short-term technical scenario

# Generated Chart
Include the generated chart image path exactly as returned by the chart generation tool.

Requirements:
- Use Markdown headings.
- Use tables for numerical indicators.
- Explain every indicator before interpreting it.
- Clearly distinguish numerical analysis from visual observations.
- Preserve the generated chart path exactly.
- Do not provide Buy/Hold/Sell recommendations.
"""),
    agent=technical_agent,
)
