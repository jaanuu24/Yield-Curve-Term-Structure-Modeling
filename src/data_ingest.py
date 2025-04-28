import pandas as pd
import sqlalchemy
import requests
from bs4 import BeautifulSoup

def load_from_sql(conn_str: str, query: str) -> pd.DataFrame:
    engine = sqlalchemy.create_engine(conn_str)
    return pd.read_sql_query(query, engine)

def load_from_api(url: str, params: dict = None) -> pd.DataFrame:
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return pd.DataFrame(resp.json())

def load_from_web_scrape(target_url: str, table_id: str) -> pd.DataFrame:
    resp = requests.get(target_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', id=table_id)
    return pd.read_html(str(table))[0]

def load_from_csv(path: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **kwargs)
