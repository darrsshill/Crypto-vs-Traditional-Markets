# Crypto vs Traditional Markets

**Quantitative analysis comparing Bitcoin (BTC) and the S&P 500** across correlation, crash behavior, and volatility — using 2,522 daily observations spanning January 2016 to December 2025.

**Course:** Financial Technology

---

## What This Project Does

This project answers three concrete financial questions using real market data, statistical modeling, and 11 publication-quality visualizations:

| # | Research Question | Methods Applied |
|---|-------------------|-----------------|
| 1 | Is Bitcoin correlated with the stock market? | Pearson correlation, 90-day rolling correlation, OLS regression, yearly breakdown |
| 2 | Does Bitcoin act as a hedge during market crashes? | Drawdown analysis, 3 major crash windows, BTC vs S&P 500 comparison |
| 3 | How does Bitcoin's volatility compare to equities? | Annualised volatility, rolling 30-day vol, VaR (95%), return distribution, kurtosis |

---

## Key Findings

### Correlation (RQ1)
- Overall Pearson correlation between daily BTC and S&P 500 returns: **r = 0.246** (p < 0.001) — statistically significant but moderate
- The relationship was **near-zero pre-2020**, then spiked sharply after COVID as institutional capital entered crypto
- OLS beta > 1: BTC **amplifies** S&P 500 moves rather than dampening them

### Crash Hedge Test (RQ2)

| Crash Event | S&P 500 Return | BTC Return | BTC Acted as Hedge? |
|-------------|---------------|------------|---------------------|
| Q4 2018 Sell-Off | -19.15% | -36.26% | No |
| COVID Crash (Feb–Mar 2020) | -33.61% | -36.74% | No |
| 2022 Bear Market | -24.95% | -58.63% | No |

**Conclusion:** Bitcoin is not a reliable safe haven. It behaves as a high-risk growth asset that sells off in "risk-off" environments alongside equities.

### Volatility Comparison (RQ3)

| Metric | Bitcoin | S&P 500 |
|--------|---------|---------|
| Annualised Volatility | 66.2% | 17.9% |
| Annualised Return | 75.0% | 13.6% |
| Return/Vol Ratio (Sharpe proxy) | 1.13 | 0.76 |
| VaR — 95% daily loss limit | -6.03% | -1.65% |
| Max single-day loss | -37.2% | -12.0% |
| Volatility ratio (BTC / S&P) | **3.71×** | — |

Despite ~3.7× higher volatility, BTC delivered ~5.5× the annualised return — an asymmetric risk/reward profile over the full period.

### Annual Total Returns

| Year | BTC | S&P 500 |
|------|-----|---------|
| 2016 | +116% | +8% |
| 2017 | **+1,425%** | +19% |
| 2018 | -74% | -6% |
| 2019 | +92% | +29% |
| 2020 | +303% | +16% |
| 2021 | +60% | +27% |
| 2022 | -64% | -19% |
| 2023 | +154% | +24% |
| 2024 | +122% | +23% |
| 2025 | -5% | +17% |

---

## Visualizations

All 11 figures are saved to [`figures/`](figures/) and generated automatically when the notebook is run.

| Figure | Description |
|--------|-------------|
| `fig1_price_history.png` | Bitcoin and S&P 500 absolute price history (2016–2025) |
| `fig2_cumulative_growth.png` | $100 invested in Jan 2016 — log-scale growth comparison |
| `fig3_correlation_heatmap.png` | Pearson correlation heatmap of daily returns |
| `fig4_rolling_correlation.png` | 90-day rolling correlation with positive/negative shading |
| `fig5_scatter_regression.png` | Scatter plot of daily returns with OLS regression line |
| `fig6_yearly_correlation.png` | BTC–S&P 500 correlation broken down by year |
| `fig7_crash_comparison.png` | Side-by-side return comparison across 3 major crashes |
| `fig8_drawdown.png` | Drawdown-from-peak charts for both assets (crash windows highlighted) |
| `fig9_rolling_volatility.png` | 30-day rolling annualised volatility over time |
| `fig10_annual_volatility.png` | Annual volatility bar chart by year |
| `fig11_return_distribution.png` | Daily return histogram + KDE for both assets |

---

## Technical Stack

| Category | Tools |
|----------|-------|
| Language | Python 3 |
| Data Sources | Yahoo Finance (`yfinance`), FRED Federal Reserve (`pandas_datareader`) |
| Data Manipulation | `pandas`, `numpy` |
| Statistics | `scipy` (Pearson r, KDE), `statsmodels` (OLS regression) |
| Visualization | `matplotlib`, `seaborn` |
| Environment | Jupyter Notebook |

### Skills Demonstrated
- **Data engineering:** Merging heterogeneous time-series from two independent APIs, forward-filling gaps, inner-join alignment on trading days
- **Statistical analysis:** Hypothesis testing (Pearson r + p-values), OLS regression, rolling statistics, groupby aggregation
- **Financial analytics:** Drawdown analysis, Value at Risk (VaR), annualised volatility, Sharpe-proxy ratios
- **Data visualization:** 11 publication-quality figures with dual-axis plots, KDE overlays, annotated bar charts, log-scale charts

---

## Project Structure

```
Crypto-vs-Traditional-Markets/
├── notebooks/
│   └── Crypto_vs_Traditional_Markets.ipynb   # Full analysis (main entry point)
├── src/
│   └── crypto_analysis.py                    # Standalone Python script (lightweight version)
├── figures/                                  # 11 generated PNG charts
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
├── presentation/
│   └── Crypto_vs_Traditional_Markets.pptx   # Slide deck
├── docs/
│   └── Final Project Guideline.pdf
├── data/                                     # Raw / cached data (git-ignored)
├── requirements.txt
└── README.md
```

---

## Setup & Run

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

Figures are saved to `figures/` automatically when all cells are run. Data is fetched live from Yahoo Finance and FRED — no local data files required.

**Alternatively, run the standalone script:**

```bash
python src/crypto_analysis.py
```

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `pandas` | ≥ 2.0 | Time-series data manipulation and alignment |
| `numpy` | ≥ 1.24 | Numerical computation and volatility calculations |
| `yfinance` | ≥ 0.2 | Bitcoin price data from Yahoo Finance |
| `pandas-datareader` | ≥ 0.10 | S&P 500 data from Federal Reserve (FRED) |
| `matplotlib` | ≥ 3.7 | Chart generation and figure export |
| `seaborn` | ≥ 0.12 | Statistical visualization (heatmap, KDE plots) |
| `scipy` | ≥ 1.10 | Pearson correlation, Gaussian KDE |
| `statsmodels` | ≥ 0.14 | OLS regression with summary statistics |
| `jupyter` | ≥ 1.0 | Interactive notebook environment |

---

## Limitations & Future Work

**Limitations:**
- Analysis covers price data only — no sentiment, regulatory events, or fundamentals
- Bitcoin alone does not represent the full crypto market (Ethereum, DeFi, altcoins excluded)
- Correlations are time-varying and unstable — past patterns may not persist

**Future extensions:**
- Add Gold and Bonds as additional comparison assets
- Incorporate Ethereum and altcoin indices
- Apply GARCH models for dynamic volatility estimation
- Use regime-switching models to capture structural correlation shifts
- Integrate sentiment data (Crypto Fear & Greed Index, Google Trends)
