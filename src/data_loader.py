import pandas as pd

def load_sales_data():
    df = pd.read_csv('data/raw_sales.csv')
    return df