import pandas as pd

def load_sales_data():
    df = pd.read_csv('data/raw_sales.csv')
    return df

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
    
    return df
def clean_sales_data(df):
    initial_rows = len(df)

    df = df.dropna(subset=['product'])

    removed_rows = initial_rows - len(df)

    print('Rows removed due to missing product:',removed_rows)

    return df
def calculate_sales_data(df):
    df['total_price'] = df['quantity'] * df['unit_price']
    return df
def generate_sales_report(df):
    total_revenue = df['total_price'].sum()

    sales_by_product = df.groupby('product')['total_price'].sum()

    return total_revenue,sales_by_product
def main():

    try:
        df = load_sales_data()
        df = clean_sales_data(df)
        df = validate_sales_data(df)
        df = calculate_sales_data(df)

        missing_values = df.isnull().sum()
        print('Missing values by column:')
        print(missing_values)

        df.to_csv('data/processed_sales.csv',index=False)
        print('Processed data saved successfully.')

        total_revenue, sales_by_product = generate_sales_report(df)

        print(df)
        print('Number of sales:',len(df))
        print('Total revenue:',total_revenue)
        print('Revenue by product: ')
        print(sales_by_product)
    except(ValueError,TypeError,FileNotFoundError) as error:
        print(f'Pipeline failed: {error}')

if __name__ == '__main__':
    main()