import pandas as pd
from src.data_loader import load_sales_data
from src.data_validator import validate_sales_data
from src.data_cleaner import clean_sales_data
from src.sales_report import calculate_sales_data, generate_sales_report

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
    except(ValueError, TypeError, FileNotFoundError) as error:
        print(f'Pipeline failed: {error}')

if __name__ == '__main__':
    main()