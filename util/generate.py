import os
import pandas as pd
import random
from faker import Faker

def generate_credit_card_data(num_records=1000):
    # Check if file already exists
    if os.path.exists('data/credit_card_records.csv'):
        print("Data file already exists. Skipping generation.")
        return
    
    # Initialize Faker
    fake = Faker()

    # Generate data
    data = {
        "Date": [fake.date() for _ in range(num_records)],
        "Amount": [round(random.uniform(1, 1000), 2) for _ in range(num_records)],
        "Location": [fake.city() for _ in range(num_records)],
        "Store": [fake.company() for _ in range(num_records)],
        "Fraudulent": [random.choice([True, False]) for _ in range(num_records)]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
        
    # Save to CSV
    df.to_csv('data/credit_card_records.csv', index=False)
    print(f"Generated {num_records} records and saved to data/credit_card_records.csv")

if __name__ == "__main__":
    generate_credit_card_data()