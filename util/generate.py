import os
import pandas as pd
import random
from faker import Faker
# add logger
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)    
# add timestamp to the log
logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add file handler
file_handler = logging.FileHandler('credit_card_records.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler) 


def generate_credit_card_data(num_records=1000):
    # Check if file already exists
    logger.info("Generating credit card data...")
    if os.path.exists('data/credit_card_records.csv'):
        logger.info("Data file already exists. Skipping generation.")
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
    logger.info(f"Generated {num_records} records")
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
        
    # Save to CSV
    df.to_csv('data/credit_card_records.csv', index=False)
    logger.info(f"Generated {num_records} records and saved to data/credit_card_records.csv")

if __name__ == "__main__":
    generate_credit_card_data()