import pandas as pd
from datetime import datetime

def year_fraction(dates: pd.Series) -> pd.Series:
    """Compute fraction of years since the earliest date."""
    start = dates.min()
    return (dates - start).dt.days / 365.25

def save_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
    print(f"Saved CSV to {path}")

def plot_term_structure(tenors, yields, title="Term Structure"):
    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(tenors, yields, marker="o")
    plt.title(title)
    plt.xlabel("Tenor (years)")
    plt.ylabel("Yield")
    plt.show()
