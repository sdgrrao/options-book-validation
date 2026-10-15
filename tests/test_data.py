import pandas as pd
import pytest

VOL_SERIES = ["vix", "vix3m", "vix6m"]
ALL_SERIES = ["spx"] + VOL_SERIES


def load(name):
    df = pd.read_csv(f"data/raw/{name}_daily.csv", index_col="date", parse_dates=True)
    return df["close"]


@pytest.mark.parametrize("name", ALL_SERIES)
def test_series_clean(name):
    s = load(name)
    assert s.index.is_monotonic_increasing
    assert not s.index.has_duplicates
    assert s.notna().all()
    assert (s > 0).all()


@pytest.mark.parametrize("name", ALL_SERIES)
def test_covers_2008_stress_window(name):
    s = load(name)
    assert s.index[0] <= pd.Timestamp("2008-09-01"), f"{name} starts {s.index[0].date()}"


def test_spx_known_crisis_days():
    r = load("spx").pct_change()
    assert r.loc["2008-10-13"] == pytest.approx(0.1158, abs=0.0005)
    assert r.loc["2020-03-16"] == pytest.approx(-0.1198, abs=0.0005)


@pytest.mark.parametrize("name", VOL_SERIES)
def test_spx_dates_covered_by_vol_series(name):
    s = load("spx")
    v = load(name)
    s = s[s.index >= v.index[0]]
    missing = s.index.difference(v.index)
    assert missing.empty, f"{len(missing)} S&P 500 dates missing from {name}: {[d.date() for d in missing[:5]]}"
