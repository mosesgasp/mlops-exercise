import numpy as np
import os
from datetime import datetime, timedelta

import pandas as pd

def generate_credit_card_data(num_records=1000):
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Generate random data
    np.random.seed(42)
    
    # Generate dates
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=x) for x in range(num_records)]
    
    # Generate random amounts
    amounts = np.random.uniform(10, 1000, num_records)
    
    # Generate random locations
    locations = np.random.choice(['New York', 'London', 'Tokyo', 'Paris', 'Sydney'], num_records)
    
    # Generate random stores
    stores = np.random.choice(['Amazon', 'Walmart', 'Target', 'Best Buy', 'Apple Store'], num_records)
    
    # Generate random fraudulent flags (with 5% being fraudulent)
    fraudulent = np.random.choice([0, 1], num_records, p=[0.95, 0.05])
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Amount': amounts,
        'Location': locations,
        'Store': stores,
        'Fraudulent': fraudulent
    })
    
    # Save to CSV
    df.to_csv('data/credit_card_records_enhanced.csv', index=False)
    print(f"Generated {num_records} records and saved to data/credit_card_records.csv")

if __name__ == "__main__":
    generate_credit_card_data()