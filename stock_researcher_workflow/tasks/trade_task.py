from crewai import Task
from ..agents.trader_agent import trader_agent

from .analyse_task import get_stock_analysis
from .fundamental_task import get_fundamentals_analysis
from .technical_task import get_technical_analysis
from .news_task import get_news_sentiment
from .risk_task import get_risk_assessment


trade_decision = Task(
    description=("""
You are acting as the final investment decision maker for the company: {stock}.

Your ONLY source of information is the outputs produced by the Market Analysis,
Fundamental Analysis, Technical Analysis, News & Sentiment Analysis, and Risk
Assessment agents.

Do NOT retrieve new information.
Do NOT perform additional market research.
Do NOT invent financial metrics or assumptions.

Your responsibility is to critically evaluate the evidence provided by every
specialist and transform it into a single investment recommendation.

Required decision-making workflow:

1. Review every specialist report completely.

2. Identify the strongest bullish arguments.

3. Identify the strongest bearish arguments.

4. Identify any conflicting conclusions between analysts.

5. Explain why certain evidence deserves greater weight than others.

6. Evaluate:
   - Market position
   - Financial quality
   - Valuation
   - Technical momentum
   - News & sentiment
   - Risk profile

7. Determine whether the overall evidence supports:
   - Buy
   - Hold
   - Sell

Do NOT simply count bullish and bearish signals.

Instead, evaluate:
- Quality of evidence
- Reliability of evidence
- Time horizon
- Magnitude of impact
- Confidence of each conclusion

If the available evidence is mixed or insufficient,
prefer a Hold recommendation instead of forcing Buy or Sell.

Every conclusion must reference the supporting specialist analysis.
"""),
    expected_output=("""
Return a professional Markdown investment recommendation with the following sections.

# Executive Summary
- Recommendation (Buy / Hold / Sell)
- Conviction Level (Very High / High / Moderate / Low)
- Investment Horizon
- Overall Investment Thesis

# Evidence Summary

Summarize the key findings from:

## Market Analysis
- Most important observations

## Fundamental Analysis
- Financial strengths
- Financial weaknesses
- Valuation conclusion

## Technical Analysis
- Trend
- Momentum
- Support / Resistance
- Technical outlook

## News & Sentiment Analysis
- Major catalysts
- Overall sentiment
- Important developments

## Risk Assessment
- Major risks
- Overall risk profile

# Bullish Factors

List and explain the strongest factors supporting the investment.

# Bearish Factors

List and explain the strongest risks or concerns.

# Conflicting Signals

Identify disagreements between specialist analyses.

Explain:
- Why they conflict
- Which evidence is more reliable
- How the conflict affects confidence

# Investment Thesis

Provide a detailed explanation of:

- Why the recommendation is appropriate
- Key drivers supporting the decision
- Major risks to monitor
- Events that would invalidate the thesis

# Target Price

Include:
- Current Price
- Expected Price Range
- Expected Upside / Downside
- Justification for the target

# Portfolio Considerations

Discuss:
- Suitable investor profile
- Suggested investment horizon
- Suggested position sizing based on the assessed risk profile

# Final Recommendation

Summarize:

- Recommendation
- Conviction Level
- Target Price Range
- Investment Horizon
- Top 3 reasons supporting the decision
- Top 3 risks investors should monitor

Requirements:

- Use professional Markdown formatting.
- Support every conclusion using the specialist analyses.
- Clearly distinguish facts from interpretation.
- Do not introduce new information.
- Do not repeat large sections from previous reports.
- Produce a concise but comprehensive institutional-quality investment recommendation.
"""),
    agent=trader_agent,
    context=[
        get_stock_analysis,
        get_fundamentals_analysis,
        get_technical_analysis,
        get_news_sentiment,
        get_risk_assessment,
    ],
)
