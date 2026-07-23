from crewai import Task
from ..agents.risk_agent import risk_agent


get_risk_assessment = Task(
    description=("""
Conduct a comprehensive risk assessment for the publicly traded company: {stock}.

Use the available quantitative risk analysis tools to evaluate the company's market risk based on
historical price data and calculated risk metrics. Assess the stock's sensitivity to broader market
movements, historical volatility, downside exposure, and overall risk profile.

Focus ONLY on quantitative market risk analysis.

Do NOT perform:
- Fundamental analysis
- Technical indicator analysis
- News or sentiment analysis
- Valuation analysis
- Investment recommendations

Calculate and analyze all available quantitative risk metrics. For every metric:

- Report the calculated value.
- Explain what the metric measures.
- Explain why investors monitor it.
- Interpret whether the current value indicates Low, Moderate, or High risk.

Support every conclusion with quantitative evidence.

If sufficient historical data is unavailable for any calculation, clearly mention the limitation
instead of estimating values.

Present the report using professional Markdown headings, tables, and bullet points.
"""),
    expected_output=("""
Return a professional Markdown report containing the following sections:

# Overall Risk Profile
- Overall Risk Rating (Low / Moderate / High)
- Confidence Level
- Brief summary of the company's market risk profile

# Beta Analysis
- Beta value
- Benchmark used
- Interpretation
- Market sensitivity

# Volatility Analysis
- Annualized Volatility
- Historical Volatility
- Interpretation
- Comparison with typical equity volatility

# Drawdown Analysis
- Maximum Drawdown
- Period analyzed
- Recovery observations
- Downside characteristics

# Historical Price Risk
- Price stability
- Significant periods of volatility
- Notable market events reflected in price movement

# Key Risk Observations
- Primary sources of market risk
- Positive observations
- Potential concerns

# Overall Risk Assessment
Provide a balanced conclusion covering:
- Overall market risk level
- Suitability for conservative, moderate, and aggressive investors
- Major quantitative risks investors should monitor

Requirements:
- Use Markdown headings.
- Use tables for numerical data.
- Include exact calculated values.
- Explain every metric before interpreting it.
- Clearly distinguish factual calculations from interpretation.
- Do not provide Buy/Hold/Sell recommendations.
"""),
    agent=risk_agent,
)
