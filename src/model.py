import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline

def fit_term_structure(x: np.ndarray, y: np.ndarray) -> CubicSpline:
    # convert dates to year fractions
    
    return CubicSpline(x, y, extrapolate=True)

def monte_carlo_scenarios(curve_func, tenors: np.ndarray,
                          n_scenarios: int = 1000,
                          vol: float = 0.01) -> np.ndarray:
    base = curve_func(tenors)
    shocks = np.random.normal(0, vol, size=(n_scenarios, len(tenors)))
    return base + shocks

if __name__ == "__main__":
    df = pd.read_csv("../data/combined_yields.csv", parse_dates=["date"])
    today = df["date"].max()
    sample = df[df["date"] == today]
    cs = fit_term_structure(sample["date"], sample["yield_10y"])
    tenors = np.array([1, 2, 5, 10])
    scenarios = monte_carlo_scenarios(cs, tenors, n_scenarios=100)
    pd.DataFrame(scenarios, columns=tenors).to_csv("../data/yield_scenarios.csv", index=False)
