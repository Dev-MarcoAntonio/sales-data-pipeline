def calculate_sales_data(df):
    df['total_price'] = df['quantity'] * df['unit_price']
    return df
def generate_sales_report(df):
    total_revenue = df['total_price'].sum()

    sales_by_product = df.groupby('product')['total_price'].sum()

    return total_revenue,sales_by_product