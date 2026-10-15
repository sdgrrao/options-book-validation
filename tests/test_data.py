import pandas as pd
import pytest


def load(name):
    df = pd.read_csv(f"data/raw/{name}_daily.csv", index_col="date", parse_dates=True)
    return df["close"]


@pytest.mark.parametrize("name", ["spx", "vix"])
def test_series_clean(name):
    s = load(name)
    assert s.index.is_monotonic_increasing
    assert not s.index.has_duplicates
    assert s.notna().all()
    assert (s > 0).all()
    assert len(s) > 5000


def test_spx_known_crisis_days():
    r = load("spx").pct_change()
    assert r.loc["2008-10-13"] == pytest.approx(0.1158, abs=0.0005)
    assert r.loc["2020-03-16"] == pytest.approx(-0.1198, abs=0.0005)


def test_spx_dates_subset_of_vix():
    s = load("spx")
    v = load("vix")
    assert s.index.difference(v.index).empty
