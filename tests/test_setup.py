from scipy.stats import norm


def test_environment():
    assert abs(norm.cdf(0) - 0.5) < 1e-12
