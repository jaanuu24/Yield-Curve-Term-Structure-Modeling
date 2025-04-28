# Yield Curve & Term Structure Modeling

A complete end-to-end toolkit for ingesting market yields, fitting a cubic-spline term structure, evaluating model performance, and generating Monte Carlo scenarios for risk analysis.

## Project Structure

```
yield-curve-model/
├── data/                     # raw inputs and generated outputs
│   └── combined_yields.csv   # sample combined yield data
├── notebooks/                # exploratory and demonstration notebooks
│   └── yield_curve_full.ipynb
├── src/                      # core Python modules
│   ├── data_ingest.py        # load from SQL, API, web scrape, or CSV
│   ├── model.py              # spline fit & Monte Carlo scenario functions
│   └── utils.py              # helpers (year fractions, plotting, saving)
├── requirements.txt          # Python dependencies
└── README.md                 # this file
```

## Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/yield-curve-model.git
   cd yield-curve-model
   ```
2. Create and activate a virtual environment  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

## Data

Place your raw or downloaded yield data in `data/combined_yields.csv`. The file must contain at least:

| column      | type    | description                        |
|-------------|---------|------------------------------------|
| `date`      | date    | YYYY-MM-DD                         |
| `yield_1y`  | float   | 1-year tenor yield (decimal form)  |
| `yield_2y`  | float   | 2-year tenor yield                 |
| `yield_5y`  | float   | 5-year tenor yield                 |
| `yield_10y` | float   | 10-year tenor yield                |

A 100-row synthetic sample is provided as `data/combined_yields_100.csv` for quick testing.

## Usage

### 1. Data Ingestion  
```bash
python -c "from src.data_ingest import load_from_csv; import pandas as pd; df=load_from_csv('data/combined_yields.csv', parse_dates=['date']); print(df.head())"
```

### 2. Term Structure Fit & Scenario Generation  
```bash
python -c "from src.model import fit_term_structure, monte_carlo_scenarios; import numpy as np, pandas as pd; df=pd.read_csv('data/combined_yields.csv', parse_dates=['date']); row=df[df.date==df.date.max()].iloc[0]; tenors=np.array([1,2,5,10]); ys=row[['yield_1y','yield_2y','yield_5y','yield_10y']].values; cs=fit_term_structure(tenors, ys); scenarios=monte_carlo_scenarios(cs, tenors, n_scenarios=100); pd.DataFrame(scenarios, columns=tenors).to_csv('data/yield_scenarios.csv', index=False)"
```

### 3. Jupyter Notebook  
Launch and explore:
```bash
jupyter lab notebooks/yield_curve_full.ipynb
```

It walks through:
- Summary statistics  
- Cubic-spline fitting  
- Cross-sectional RMSE backtest  
- Monte Carlo scenario analysis  
- Histogram and summary tables

## Utilities

- `src/utils.py` includes functions for  
  - computing year-fractions  
  - plotting term-structures  
  - saving CSVs with a confirmation message  

Feel free to import and extend them in your own scripts.

## Contributing

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/...`)  
3. Commit your changes  
4. Open a pull request

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
