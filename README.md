# Crypto vs Traditional Markets

Quantitative analysis comparing **Bitcoin (BTC)** and the **S&P 500** across correlation, crash behavior, and volatility — using daily price data from January 2016 to December 2025.

**Course:** Financial Technology

---

## Research Questions

| # | Question | Methods |
|---|----------|---------|
| 1 | Is Bitcoin correlated with the stock market? | Pearson correlation, 90-day rolling correlation, OLS regression, yearly breakdown |
| 2 | Does Bitcoin act as a hedge during market crashes? | Drawdown analysis, 5 worst S&P 500 crash windows, BTC performance comparison |
| 3 | How does Bitcoin's volatility compare to equities? | Annualised historical volatility, rolling 30-day vol, VaR (95%), return distribution |

---

## Data Sources

| Asset | Source | Access |
|-------|--------|--------|
| Bitcoin (BTC-USD) | Yahoo Finance | `yfinance` |
| S&P 500 Index | Federal Reserve (FRED) | `pandas_datareader` |

Both series are aligned on matching business days (inner join). S&P 500 gaps from FRED (non-trading days) are forward-filled before merging.

---

## Project Structure

```
Crypto-vs-Traditional-Markets/
├── data/                   # Raw / cached data (git-ignored)
├── docs/
│   └── Final Project Guideline.pdf
├── figures/                # Generated charts (11 PNGs)
│   ├── fig1_price_history.png
│   ├── fig2_cumulative_growth.png
│   ├── fig3_correlation_heatmap.png
│   ├── fig4_rolling_correlation.png
│   ├── fig5_scatter_regression.png
│   ├── fig6_yearly_correlation.png
│   ├── fig7_crash_comparison.png
│   ├── fig8_drawdown.png
│   ├── fig9_rolling_volatility.png
│   ├── fig10_annual_volatility.png
│   └── fig11_return_distribution.png
├── notebooks/
│   └── Crypto_vs_Traditional_Markets.ipynb   # Main analysis
├── presentation/
│   └── Crypto_vs_Traditional_Markets.pptx
├── src/
│   └── crypto_analysis.py  # Standalone Python script
├── requirements.txt
└── README.md
```

---

## Setup

**1. Create and activate a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Launch the notebook**

```bash
jupyter notebook notebooks/Crypto_vs_Traditional_Markets.ipynb
```

> Figures are saved to `figures/` automatically when cells are run.

---

## Key Findings

- **Correlation** between BTC and S&P 500 daily returns is positive but moderate overall, with the relationship being near-zero pre-2020 and rising sharply post-COVID as institutional capital entered crypto markets.
- **Crash hedge** — Bitcoin did not consistently act as a safe haven. During major S&P 500 drawdowns (COVID March 2020, 2022 rate-hike bear market), BTC sold off alongside equities rather than holding value.
- **Volatility** — Bitcoin's annualised volatility is roughly 3–5× higher than the S&P 500. Its return distribution has heavier tails and higher kurtosis, meaning extreme moves (both gains and losses) are far more frequent.

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation and time-series alignment |
| `numpy` | Numerical computation |
| `yfinance` | Bitcoin price data from Yahoo Finance |
| `pandas-datareader` | S&P 500 data from FRED |
| `matplotlib` | Charting and figure export |
| `seaborn` | Statistical visualisation (heatmap, KDE) |
| `scipy` | Pearson correlation, Gaussian KDE |
| `statsmodels` | OLS regression |
| `jupyter` | Interactive notebook environment |
