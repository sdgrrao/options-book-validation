# Evidence log

Every number quoted in the report or on the CV, with where it came from.

| Date | Item | Value | Parameters / source | File |
|---|---|---|---|---|
| 2026-10-15 | S&P 500 daily closes | 5,480 rows, 2005-01-03 to 2026-10-14 | Yahoo ^GSPC via yfinance 1.7.0, Close, auto_adjust=False | data/raw/spx_daily.csv |
| 2026-10-15 | VIX daily closes | 5,482 rows, 2005-01-03 to 2026-10-14 | Yahoo ^VIX via yfinance 1.7.0, Close, auto_adjust=False | data/raw/vix_daily.csv |
| 2026-10-15 | Crisis-day check | S&P 500 +11.58% on 2008-10-13, -11.98% on 2020-03-16, within 0.05pp | Computed from closes | tests/test_data.py |
| 2026-10-15 | Data finding: partial-day row | First pull included a 2026-10-15 intraday price (run at 14:44 New York time). Script now drops rows dated on the download day | Yahoo via yfinance | scripts/download_data.py |
| 2026-10-15 | Data finding: date mismatch | VIX has 2 dates with no S&P 500 row: 2026-05-25 and 2026-09-07 (US market holidays). No S&P 500 dates missing from VIX. Align on S&P 500 dates in analysis | Raw files left unchanged | tests/test_data.py |
| 2026-10-15 | Data finding: holiday VIX values | VIX values on 2026-05-25 (16.59) and 2026-09-07 (15.30) differ from prior day (16.70, 14.53), so not carried forward. Cause not confirmed. After aligning on S&P 500 dates, post-holiday VIX change spans Fri to Tue | Yahoo ^VIX | data/raw/vix_daily.csv |
| 2026-10-15 | VIX3M daily closes | 5,094 rows, 2006-07-17 to 2026-10-14 | Yahoo ^VIX3M via yfinance 1.7.0, Close, auto_adjust=False | data/raw/vix3m_daily.csv |
| 2026-10-15 | VIX6M daily closes | 4,726 rows, 2008-01-02 to 2026-10-14 | Yahoo ^VIX6M via yfinance 1.7.0, Close, auto_adjust=False | data/raw/vix6m_daily.csv |
| 2026-10-15 | Data finding: VIX3M start date | Yahoo VIX3M starts 2006-07-17, before the 2007-12-04 start of Cboe's published history (FRED series VXVCLS). Origin of earlier values not confirmed. No effect: VIX6M starts 2008-01-02, so vol inputs are only used from that date | Yahoo ^VIX3M vs FRED VXVCLS | data/raw/vix3m_daily.csv |
| 2026-10-15 | Common vol history start | 2008-01-02, set by VIX6M. Rolling VaR needs 250 days of history after this, so the first VaR date falls around the end of 2008 | All vol series | data/raw/ |
| 2026-10-15 | Data check: date coverage | Every S&P 500 trading date from each vol series' start date is present in VIX, VIX3M and VIX6M | 13 tests passing | tests/test_data.py |
