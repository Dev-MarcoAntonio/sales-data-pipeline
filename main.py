import logging

from src.data_loader import load_sales_data
from src.data_validator import validate_sales_data
from src.data_cleaner import clean_sales_data,detect_duplicate_sales
from src.sales_report import calculate_sales_data, generate_sales_report

logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        filename='pipeline.log',
        encoding='utf-8'
    )

def main():

    try:
        logging.info('Pipeline started')
        df = load_sales_data()
        logging.info('Sales data loaded successfully')
        df = clean_sales_data(df)
        df = validate_sales_data(df)

        duplicates = detect_duplicate_sales(df)

        if not duplicates.empty:
            logging.warning(
                'Potential duplicate sales found: \n%s',
                duplicates
            )
            print('Potential duplicate sales found:')
            print(duplicates)
        else:
            logging.info('No duplicate sales found')

        df = calculate_sales_data(df)

        missing_values = df.isnull().sum()
        print('Missing values by column:')
        print(missing_values)

        df.to_csv('data/processed_sales.csv',index=False)
        logging.info('Processed data saved successfully.')

        total_revenue, sales_by_product = generate_sales_report(df)

        logging.info('Number of sales: %s',len(df))
        logging.info('Total revenue: %.2f',total_revenue)
        logging.info('Revenue by product:\n%s',sales_by_product)

        print(df)
        print('Number of sales:',len(df))
        print('Total revenue:',total_revenue)
        print('Revenue by product: ')
        print(sales_by_product)

        logging.info('Pipeline completed successfully')

    except(ValueError, TypeError, FileNotFoundError) as error:
        logging.error('Pipeline failed: %s',error)

if __name__ == '__main__':
    main()