import logging

def clean_sales_data(df):
    initial_rows = len(df)

    df = df.dropna(subset=['product']).copy()

    df['product'] = df['product'].astype(str).str.strip()

    df = df[df['product'] != ''].copy()

    removed_rows = initial_rows - len(df)

    logging.info('Rows removed due to missing product: %s',removed_rows)

    return df