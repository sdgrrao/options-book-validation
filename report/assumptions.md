# Modelling assumptions

Fixed on 15 October 2026, before any pricing code was written. Any later change is recorded in the change log at the bottom, with the reason.

## Scope

1. **Underlying.** S&P 500 price index (Yahoo ^GSPC, Close). European, cash-settled options only. The price index is used, not a total return index, because index options settle on the price index.

## Market parameters

2. **Risk-free rate.** Constant r = 4% a year, continuously compounded, flat across maturities. Tested in Phase 4.3.

3. **Dividends.** All pricers take a continuous dividend yield q. Baseline q = 0. Synthetic paths in Phases 1, 2 and 4.1 are generated under the same q, so q = 0 is internally consistent and avoids having to credit dividend income to the hedge.
   Materiality test in Phase 4.3 at q = 1.1% (approximate trailing S&P 500 yield, late 2025 to mid 2026). If 99% VaR, 97.5% ES or the standard deviation of hedging P&L changes by more than 5%, the baseline becomes q = 1.1% and this is reported as a finding. The 5% threshold is set here so it cannot be chosen after seeing the result.

## Volatility

4. **Pricing.** Constant volatility per option, flat across strikes. This is the Black-Scholes assumption the validation report tests.

5. **Real-data VaR, backtest and stress tests.** Each option's volatility is interpolated by maturity from VIX (30 calendar days), VIX3M (93 days) and VIX6M (about 6 months; confirm Cboe's stated tenor before Phase 3). Interpolation is linear in total variance (sigma^2 x T), with flat extrapolation outside the range. Historical volatility changes are applied as relative shifts: sigma_scenario = sigma_today x (sigma_t / sigma_t-1). Absolute shifts are tested in Phase 4.3.
   Known limitations:
   - VIX-family indices are variance-swap strikes, which sit above at-the-money implied volatility, so volatility levels are biased upward.
   - No volatility skew: every strike at a given maturity gets the same volatility.

## Time and returns

6. **Time.** 252 trading days a year, daily step 1/252. All maturities expressed in years.

7. **Spot scenarios.** Historical log returns applied to today's level: S_scenario = S_today x (S_t / S_t-1).

## VaR and ES

8. **Conventions.**
   - 1-day horizon. 99% VaR and 97.5% ES. 250-day equally weighted window. Losses reported as positive numbers.
   - VaR is the k-th largest loss, k = ceiling(N x (1 - alpha)). For N = 250 and 99%, that is the 3rd largest loss.
   - ES is the average of the worst N x (1 - alpha) losses, with a fractional weight on the last one. For N = 250 and 97.5%: (sum of the 6 largest losses + 0.25 x the 7th largest) / 6.25.
   - Full revaluation is the primary method. Delta-gamma approximation is the comparison.
   - Backtesting uses hypothetical P&L: the book is held fixed and revalued at the next close.
   - Basel traffic-light zone reported on the most recent 250 days.
   - Kupiec, Christoffersen and conditional coverage tests run on a rolling backtest from the first date with 250 days of history in every risk factor, for statistical power.
   - Window length (500 days) tested in Phase 4.3.

## Hedging

9. **Delta hedging.** Once a day at the close, using the model's own delta. No transaction costs or bid-ask spread. Cash account accrues at r.

## Reproducibility

10. **Seeds and data.** Every simulation uses a fixed random seed, recorded in the evidence log. The raw data snapshot is committed to the repository. The download script drops rows dated on the download day.

## Change log

| Date | Assumption | Change | Reason |
|---|---|---|---|
