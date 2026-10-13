import pandas as pd
import logging

def validate_sales_data(df):

    required_columns = {'date','product','quantity','unit_price'}
    existing_columns = set(df.columns)
    missing_columns = required_columns - existing_columns

    if missing_columns:
        raise ValueError(f'Missing required columns: {missing_columns}')
    if df['date'].isnull().any():
        raise ValueError('Date cannot be missing')
    
    dates = df['date'].astype(str)

    invalid_dates = ~dates.str.fullmatch(r'\d{4}-\d{2}-\d{2}')

    if invalid_dates.any():
        invalid_rows = df.index[invalid_dates] + 2
        invalid_values = df.loc[invalid_dates,'date']

        raise ValueError(
            f'Invalid date format at CSV rows {invalid_rows.tolist()}:'
            f'{invalid_values.tolist()}'
        )

    try:
        pd.to_datetime(df['date'], format='%Y-%m-%d', errors='raise')
    except (ValueError, TypeError) as error:
        parsed_dates = pd.to_datetime(
            df['date'],
            format='%Y-%m-%d',
            errors='coerce'
        )
        invalid_dates = parsed_dates.isnull()
        invalid_rows = df.index[invalid_dates] + 2
        invalid_values = df.loc[invalid_dates, 'date']

        raise ValueError(
            f'Invalid date values at CSV rows {invalid_rows.tolist()}: '
            f'{invalid_values.tolist()}'
        ) from error

    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='raise')

    original_quantity = df['quantity'].copy()
    missing_quantity = original_quantity.isnull()

    if missing_quantity.any():
        raise ValueError('Quantity cannot be missing')

    df['quantity'] = pd.to_numeric(df['quantity'],errors='coerce')
    invalid_quantity = df['quantity'].isnull()
    invalid_rows = df.index[invalid_quantity] + 2
    invalid_values = original_quantity[invalid_quantity]

    if invalid_quantity.any():
        raise ValueError(
            f'Invalid quantity at CSV rows {invalid_rows.tolist()}:'
            f'{invalid_values.tolist()}'
        )

    original_price = df['unit_price'].copy()
    missing_price = original_price.isnull()

    if missing_price.any():
        raise ValueError('Unit price cannot be missing')

    df['unit_price'] = pd.to_numeric(original_price,errors='coerce')

    invalid_price = df['unit_price'].isnull()
    invalid_rows = df.index[invalid_price] + 2
    invalid_values = original_price[invalid_price]

    if invalid_price.any():
        raise ValueError(
            f'Invalid unit price at CSV rows {invalid_rows.tolist()}:'
            f'{invalid_values.tolist()}'
        )
    
    if (df['quantity'] <= 0).any():
        raise ValueError('Quantity must be greater than zero')

    if (df['unit_price'] < 0 ).any():
        raise ValueError('Unit price cannot be negative')

    logging.info('Sales data validation completed successfully')
    
    return df