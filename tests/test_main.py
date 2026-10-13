import pandas as pd
import pytest

from main import validate_sales_data,clean_sales_data,calculate_sales_data,generate_sales_report


def test_quantity_must_be_greater_than_zero():
    df = pd.DataFrame({
        'date': ['2026-10-01'],
        'product': ['Mouse'],
        'quantity': [-2],
        'unit_price': [10.0]
    })

    with pytest.raises(ValueError, match='Quantity must be greater than zero'):
        validate_sales_data(df)

def test_unit_price_cannot_be_negative():
    df = pd.DataFrame({
        'date': ['2026-10-01'],
        'product': ['Mouse'],
        'quantity': [2],
        'unit_price': [-10.0]
    })

    with pytest.raises(ValueError, match='Unit price cannot be negative'):
        validate_sales_data(df)

def test_quantity_must_be_numeric():
    df = pd.DataFrame({
        'date': ['2026-10-01'],
        'product': ['Mouse'],
        'quantity': ['abc'],
        'unit_price': [10.0]
    })

    with pytest.raises(ValueError, match='Invalid quantity at CSV rows'):
        validate_sales_data(df)

def test_quantity_cannot_be_missing():
    df = pd.DataFrame({
        'date': ['2026-10-01'],
        'product': ['Mouse'],
        'quantity': [None],
        'unit_price': [10.0]
    })

    with pytest.raises(ValueError, match='Quantity cannot be missing'):
        validate_sales_data(df)

def test_clean_sales_data_removes_missing_products():
    df = pd.DataFrame({
        'product': ['Keyboard', None, 'Mouse'],
        'quantity': [2, 1, 3],
        'unit_price': [120.0, 50.0, 50.0]
    })

    cleaned_df = clean_sales_data(df)

    assert len(cleaned_df) == 2
    assert cleaned_df['product'].isnull().sum() == 0

def test_calculate_sales_data():
    df = pd.DataFrame({
        'product': ['Keyboard', 'Mouse'],
        'quantity': [2, 3],
        'unit_price': [120.0, 50.0]
    })

    result = calculate_sales_data(df)

    assert result['total_price'].tolist() == [240.0, 150.0]

def test_generate_sales_report():
    df = pd.DataFrame({
        'product': ['Keyboard', 'Mouse', 'Keyboard'],
        'total_price': [240.0, 150.0, 120.0]
    })

    total_revenue, sales_by_product = generate_sales_report(df)

    assert total_revenue == 510.0
    assert sales_by_product['Keyboard'] == 360.0
    assert sales_by_product['Mouse'] == 150.0

from unittest.mock import patch

from main import load_sales_data


def test_load_sales_data_file_not_found():
   with patch('src.data_loader.pd.read_csv', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            load_sales_data()

def test_validate_missing_columns():
    import pandas as pd
    import pytest
    from src.data_validator import validate_sales_data

    df = pd.DataFrame({
        'product': ['Mouse'],
        'quantity': [2],
    })

    with pytest.raises(ValueError, match = 'Missing required columns'):
        validate_sales_data(df)

def test_validate_invalid_date_format():
    df = pd.DataFrame({
        'date': ['20-12-2026'],
        'product': ['Mouse'],
        'quantity': [2],
        'unit_price': [20.0]
    })
    with pytest.raises(ValueError, match= 'Invalid date format at CSV rows'):
        validate_sales_data(df)

def test_validate_impossible_date():
    df = pd.DataFrame({
        'date': ['2026-12-38'],
        'product': ['Mouse'],
        'quantity': [2],
        'unit_price': [20.0]
    })
    with pytest.raises(ValueError, match='Invalid date values at CSV rows'):
        validate_sales_data(df)

def test_validate_missing_date():
    df = pd.DataFrame({
        'date': [None],
        'product': ['Mouse'],
        'quantity': [2],
        'unit_price': [50.0]
    })

    with pytest.raises(ValueError, match='Date cannot be missing'):
        validate_sales_data(df)

def test_validate_invalid_date_reports_csv_row_and_value():
    df = pd.DataFrame({
        'date': ['2026-10-01','20-12-2026','2026-10-03'],
        'product': ['Keyboard','Mouse','Monitor'],
        'quantity': [2,3,1],
        'unit_price': [120.0,50.0,850.0]
    })

    with pytest.raises(ValueError) as error:
        validate_sales_data(df)

    assert 'CSV rows [3]' in str(error.value)
    assert '20-12-2026' in str(error.value)

def test_validate_impossible_date_reports_csv_row_and_value():
    df = pd.DataFrame({
        'date': ['2026-10-01', '2026-15-40', '2026-10-03'],
        'product': ['Keyboard', 'Mouse', 'Monitor'],
        'quantity': [2, 3, 1],
        'unit_price': [120.0, 50.0, 850.0]
    })

    with pytest.raises(ValueError) as error:
        validate_sales_data(df)

    assert 'CSV rows [3]' in str(error.value)
    assert "['2026-15-40']" in str(error.value)

def test_unit_price_must_be_numeric_reports_csv_row_and_value():
    df = pd.DataFrame({
        'date': ['2026-10-01'],
        'product': ['Mouse'],
        'quantity': [2],
        'unit_price': ['abc']
    })

    with pytest.raises(ValueError) as error:
        validate_sales_data(df)

    assert 'Invalid unit price at CSV rows [2]' in str(error.value)
    assert "['abc']" in str(error.value)

def test_unit_price_cannot_be_missing():
    df = pd.DataFrame({
        'date': ['2026-10-01'],
        'product': ['Mouse'],
        'quantity': [2],
        'unit_price': [None]
    })
    with pytest.raises(ValueError, match= 'Unit price cannot be missing'):
        validate_sales_data(df)

def test_clean_sales_data_removes_empty_product():
    df = pd.DataFrame({
        'product': ['Keyboard','    ','','Mouse'],
        'quantity': [2,1,3,2],
        'unit_price': [120.0, 50.0, 30.0, 50.0]
    })

    cleaned_df = clean_sales_data(df)

    assert len(cleaned_df) == 2
    assert cleaned_df['product'].tolist() == ['Keyboard','Mouse']