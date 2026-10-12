def clean_sales_data(df):
    initial_rows = len(df)

    df = df.dropna(subset=['product'])

    removed_rows = initial_rows - len(df)

    print('Rows removed due to missing product:',removed_rows)

    return df