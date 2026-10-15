"""Download daily S&P 500 and VIX closes from Yahoo Finance into data/raw.

Rows dated on the download day are dropped: if the US market is still open,
that row is an intraday price, not a close.
"""
from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf

START = "2005-01-01"
RAW = Path("data/raw")


def fetch_close(ticker: str) -> pd.Series:
    hist = yf.Ticker(ticker).history(start=START, auto_adjust=False)
    if hist.empty:
        raise RuntimeError(f"No data returned for {ticker}")
    close = hist["Close"].copy()
    if close.index.tz is not None:
        close.index = close.index.tz_localize(None)
    close.index = close.index.normalize()
    close = close[close.index < pd.Timestamp(date.today())]
    close.name = "close"
    return close


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    for ticker, name in [("^GSPC", "spx"), ("^VIX", "vix")]:
        close = fetch_close(ticker)
        path = RAW / f"{name}_daily.csv"
        close.to_csv(path, index_label="date")
        print(f"{ticker}: {len(close)} rows, "
              f"{close.index[0].date()} to {close.index[-1].date()} -> {path}")
    print(f"Downloaded on {date.today()}")


if __name__ == "__main__":
    main()
