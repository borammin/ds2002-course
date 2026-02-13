#!/usr/bin/env python3

import sys
import os
import time
import logging
import requests
import pandas as pd
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def extract():
    """
    Extract ISS location data from the Open Notify API.
    Returns parsed JSON data.
    """
    url = "http://api.open-notify.org/iss-now.json"
    logger.info("Extracting ISS location data")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        logger.info("Data extraction successful")
        return data
    except requests.RequestException as e:
        logger.error(f"Error extracting data: {e}")
        return None
def transform(data):
    """
    Transform raw JSON ISS data into a single-row pandas DataFrame.
    """
    logger.info("Transforming data")

    if data is None:
        logger.error("No data to transform")
        return None

    timestamp = pd.to_datetime(data["timestamp"], unit="s")
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    df = pd.DataFrame([{
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "latitude": latitude,
        "longitude": longitude
    }])

    logger.info("Data transformation complete")
    return df

def load(df, csv_file):
    """
    Load the DataFrame into a CSV file by appending records.
    """
    logger.info("Loading data into CSV")

    if df is None:
        logger.error("No data to load")
        return

    if os.path.exists(csv_file):
        existing = pd.read_csv(csv_file)
        combined = pd.concat([existing, df], ignore_index=True)
        combined.to_csv(csv_file, index=False)
    else:
        df.to_csv(csv_file, index=False)

    logger.info(f"Data written to {csv_file}")

def main():

    if len(sys.argv) != 2:
        logger.error("Usage: iss.py <output_csv>")
        sys.exit(1)

    csv_file = sys.argv[1]

    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data, csv_file)

if __name__ == "__main__":
    main()
