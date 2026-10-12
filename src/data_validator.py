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

    if not dates.str.fullmatch(r'\d{4}-\d{2}-\d{2}').all():
        raise ValueError('Date must follow YYYY-MM-DD format')

    try:
        df['date'] = pd.to_datetime(df['date'],format = '%Y-%m-%d',errors='raise')
    except(ValueError,TypeError):
        raise ValueError('Date contains invalid values')
    try:
        df['quantity'] = pd.to_numeric(df['quantity'],errors='raise')
        df['unit_price'] = pd.to_numeric(df['unit_price'],errors='raise')
    except(ValueError,TypeError):
        raise ValueError('Quantity and unit must be numeric')
    if df[['quantity', 'unit_price']].isnull().any().any():
        raise ValueError('Quantity and unit price cannot be missing')
    
    if (df['quantity'] <= 0).any():
        raise ValueError('Quantity must be greater than zero')

    if (df['unit_price'] < 0 ).any():
        raise ValueError('Unit price cannot be negative')

    logging.info('Sales data validation completed successfully')
    
    return df