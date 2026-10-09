import pandas as pd

df = pd.read_csv('data/raw_sales.csv')

missing_values = df.isnull().sum()
print('Missing values by column:')
print(missing_values)

initial_rows = len(df)

df = df.dropna(subset=["product"])

removed_rows = initial_rows - len(df)

print("Rows removed due to missing product:", removed_rows)

if (df['quantity'] <= 0).any():
    raise ValueError('Quantity must be greater than zero')

if (df['unit_price'] < 0 ).any():
    raise ValueError('Unit price cannot be negative')

df['total_price'] = df['quantity'] * df['unit_price']

df.to_csv('data/processed_sales.csv',index=False)
print('Processed data saved successfully.')

total_revenue = df['total_price'].sum()

sales_by_product = df.groupby('product')['total_price'].sum()

print(df)
print('Number of sales:',len(df))
print('Total revenue:',total_revenue)
print('Revenue by product: ')
print(sales_by_product)