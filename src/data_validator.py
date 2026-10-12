import pandas as pd
import logging

def validate_sales_data(df):
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