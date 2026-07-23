from crewai import Task
from ..agents.fundamental_agent import fundamentals_agent

get_fundamentals_analysis = Task(
    description=("""
Conduct a comprehensive fundamental analysis of the publicly traded company: {stock}.

Use the available financial statements and financial ratio tools to evaluate the company's
financial health, profitability, growth, balance sheet strength, cash generation, and valuation.

Your objective is to determine whether the company's fundamentals indicate a financially
strong, average, or weak business, and whether the stock appears undervalued, fairly valued,
or overvalued based solely on the available financial data.

Focus ONLY on fundamental analysis.

Do NOT discuss:
- Technical indicators
- Price charts
- News or sentiment
- Market risk
- Trading recommendations

For every important financial metric:
- Report the actual value.
- Explain what the metric measures.
- Explain why investors monitor it.
- Interpret whether the value is favorable, neutral, or unfavorable.

Support every conclusion using financial evidence.
If any financial metric is unavailable, explicitly state that instead of making assumptions.

Present the analysis using professional Markdown headings, tables, and bullet points.
"""),
    expected_output=("""
Return a professional Markdown report containing the following sections:

# Company Financial Overview
- Business summary
- Industry (if available)

# Income Statement Analysis
- Revenue
- Revenue Growth
- Net Income
- EPS
- Operating Income
- Profitability Trends

# Balance Sheet Analysis
- Total Assets
- Total Liabilities
- Cash & Cash Equivalents
- Debt
- Shareholders' Equity
- Debt-to-Equity
- Liquidity Assessment

# Cash Flow Analysis
- Operating Cash Flow
- Investing Cash Flow
- Financing Cash Flow
- Free Cash Flow (if available)

# Profitability Metrics
- Gross Margin
- Operating Margin
- Net Margin
- ROE
- ROA
- ROIC (if available)

# Valuation Metrics
- P/E Ratio
- Forward P/E (if available)
- PEG Ratio (if available)
- Price-to-Book
- EV/EBITDA (if available)
- Price-to-Sales (if available)

# Financial Strength
- Key strengths supported by data
- Key weaknesses supported by data

# Overall Fundamental Assessment
Provide a balanced conclusion explaining:
- Financial health
- Profitability
- Growth quality
- Valuation
- Overall fundamental outlook

Requirements:
- Use Markdown headings.
- Use tables for numerical data.
- Explain every metric before interpreting it.
- Include exact numerical values whenever available.
- Clearly distinguish factual observations from interpretation.
- Do not include Buy/Hold/Sell recommendations.
"""),
    agent=fundamentals_agent,
)
