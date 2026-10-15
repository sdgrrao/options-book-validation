# Evidence log

Every number quoted in the report or on the CV, with where it came from.

| Date | Item | Value | Parameters / source | File |
|---|---|---|---|---|
| 2026-10-15 | S&P 500 daily closes | 5,480 rows, 2005-01-03 to 2026-10-14 | Yahoo ^GSPC via yfinance 1.7.0, Close, auto_adjust=False | data/raw/spx_daily.csv |
| 2026-10-15 | VIX daily closes | 5,482 rows, 2005-01-03 to 2026-10-14 | Yahoo ^VIX via yfinance 1.7.0, Close, auto_adjust=False | data/raw/vix_daily.csv |
| 2026-10-15 | Crisis-day check | S&P 500 +11.58% on 2008-10-13, -11.98% on 2020-03-16, within 0.05pp | Computed from closes | tests/test_data.py |
| 2026-10-15 | Data finding: partial-day row | First pull included a 2026-10-15 intraday price (run at 14:44 New York time). Script now drops rows dated on the download day | Yahoo via yfinance | scripts/download_data.py |
| 2026-10-15 | Data finding: date mismatch | VIX has 2 dates with no S&P 500 row: 2026-05-25 and 2026-09-07 (US market holidays). No S&P 500 dates missing from VIX. Align on S&P 500 dates in analysis | Raw files left unchanged | tests/test_data.py |
