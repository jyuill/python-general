
# Bollinger Bands for GOOG
# - example provided by ChatGPT
# - Uses matplotlib (no seaborn, no custom colors)
# - One chart only
# - 20-day SMA and ±2 standard deviations

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Parameters
ticker = "GOOG"
lookback = 20     # N
k = 2             # number of std devs

# Download daily data (past 1 year)
data = yf.download(ticker, period="1y", interval="1d", auto_adjust=True)
close = data["Close"].copy()

# Middle band: 20-day simple moving average
mid = close.rolling(lookback, min_periods=lookback).mean()

# Rolling standard deviation (population-style to match many Bollinger definitions)
# If you prefer pandas' default sample std, remove ddof=0.
roll_std = close.rolling(lookback, min_periods=lookback).std(ddof=0)

upper = mid + k * roll_std
lower = mid - k * roll_std

# Plot
plt.figure(figsize=(10, 5))
plt.plot(close.index, close.values, label=f"{ticker} Close")
plt.plot(mid.index, mid.values, label=f"SMA {lookback}")
plt.plot(upper.index, upper.values, label=f"Upper Band (+{k}σ)")
plt.plot(lower.index, lower.values, label=f"Lower Band (-{k}σ)")

plt.title(f"{ticker} — Bollinger Bands ({lookback}, {k}σ)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.show()
