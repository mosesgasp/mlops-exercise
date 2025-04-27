import os
import pandas as pd
from util.generate import generate_credit_card_data

def test_data_generation():
    # Only generate data if file doesn't exist
    if not os.path.exists('data/credit_card_records.csv'):
        generate_credit_card_data(num_records=10)
    
    # Check if file exists
    assert os.path.exists('data/credit_card_records.csv'), "CSV file was not created"
    
    # Load the data
    df = pd.read_csv('data/credit_card_records.csv')
    
    # Check if DataFrame has correct columns
    expected_columns = ['Date', 'Amount', 'Location', 'Store', 'Fraudulent']
    assert all(col in df.columns for col in expected_columns), "Missing expected columns"
    
    # Check data types
    assert pd.api.types.is_datetime64_any_dtype(pd.to_datetime(df['Date'])), "Date column is not datetime"
    assert pd.api.types.is_numeric_dtype(df['Amount']), "Amount column is not numeric"
    assert pd.api.types.is_object_dtype(df['Location']), "Location column is not string"
    assert pd.api.types.is_object_dtype(df['Store']), "Store column is not string"
    assert pd.api.types.is_numeric_dtype(df['Fraudulent']), "Fraudulent column is not numeric"
    
    # Check value ranges
    assert df['Amount'].min() >= 1, "Amount values too low"
    assert df['Amount'].max() <= 1000, "Amount values too high"
    assert df['Fraudulent'].isin([0, 1]).all(), "Fraudulent column contains invalid values" 