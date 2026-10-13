import logging

def clean_sales_data(df):
    initial_rows = len(df)

    df = df.dropna(subset=['product']).copy()

    df['product'] = df['product'].astype(str).str.strip()

    df = df[df['product'] != ''].copy()

    removed_rows = initial_rows - len(df)

    logging.info('Rows removed due to missing product: %s',removed_rows)

    return df

def detect_duplicate_sales(df):
    duplicates = df.duplicated()

    duplicate_count = int(duplicates.sum())

    csv_rows = (df.index[duplicates] +2).tolist()

    logging.info(
        'Potential duplicate sales detected %s',
        duplicate_count
    )

    if csv_rows:
        logging.warning(
            'Potential duplicate sales found at CSV rows: %s',
            csv_rows
        )

    return df[duplicates].copy()