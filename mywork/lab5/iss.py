#!/usr/bin/env python3

import os
import logging
import requests
import mysql.connector
from datetime import datetime

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSER"),
        password=os.getenv("DBPASS"),
        database="iss"
    )

def register_reporter(reporter_id, reporter_name):
    db = None
    cursor = None
    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "SELECT reporter_id FROM reporters WHERE reporter_id = %s",
            (reporter_id,)
        )

        if cursor.fetchone() is None:
            cursor.execute(
                """
                INSERT INTO reporters (reporter_id, reporter_name)
                VALUES (%s, %s)
                """,
                (reporter_id, reporter_name)
            )
            db.commit()
            logger.info("Reporter registered")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def extract():
    url = "http://api.open-notify.org/iss-now.json"
    logger.info("Extracting ISS location data")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"API error: {e}")
        return None


def transform(data):
    if data is None:
        return None

    return {
        "message": data["message"],
        "latitude": float(data["iss_position"]["latitude"]),
        "longitude": float(data["iss_position"]["longitude"]),
        "timestamp": datetime.utcfromtimestamp(data["timestamp"])
    }

def load(record, reporter_id):
    if record is None:
        logger.error("No data to load")
        return

    db = None
    cursor = None
    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            """
            INSERT INTO locations
            (message, latitude, longitude, timestamp, reporter_id)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                record["message"],
                record["latitude"],
                record["longitude"],
                record["timestamp"],
                reporter_id
            )
        )

        db.commit()
        logger.info("Location inserted")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


def main():
    reporter_id = "tsc9rv"     
    reporter_name = "B. Min"

    register_reporter(reporter_id, reporter_name)

    raw = extract()
    record = transform(raw)
    load(record, reporter_id)

if __name__ == "__main__":
    main()
