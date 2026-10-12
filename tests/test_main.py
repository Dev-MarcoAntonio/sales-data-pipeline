import pandas as pd
import pytest

from main import validate_sales_data,clean_sales_data,calculate_sales_data,generate_sales_report


def test_quantity_must_be_greater_than_zero():
    df = pd.DataFrame({
        'quantity': [-2],
        'unit_price': [10.0]
    })

    with pytest.raises(ValueError, match='Quantity must be greater than zero'):
        validate_sales_data(df)

def test_unit_price_cannot_be_negative():
    df = pd.DataFrame({
        'quantity': [2],
        'unit_price': [-10.0]
    })

    with pytest.raises(ValueError, match='Unit price cannot be negative'):
        validate_sales_data(df)

def test_quantity_must_be_numeric():
    df = pd.DataFrame({
        'quantity': ['abc'],
        'unit_price': [10.0]
    })

    with pytest.raises(ValueError, match='Quantity and unit must be numeric'):
        validate_sales_data(df)

def test_quantity_cannot_be_missing():
    df = pd.DataFrame({
        'quantity': [None],
        'unit_price': [10.0]
    })

    with pytest.raises(ValueError, match='Quantity and unit price cannot be missing'):
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