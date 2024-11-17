import requests
import sqlite3
from datetime import datetime

API_URL = "https://api.monobank.ua/bank/currency"

connection = sqlite3.connect("exchange_rates.db")
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS exchange_rate_to_usd (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_name TEXT,
    currency_value REAL,
    current_date DATETIME
)
"""
)
connection.commit()


def get_exchange_rates():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching data from Monobank API")


def save_to_db(currency_name, currency_value):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        """
    INSERT INTO exchange_rate_to_usd /
    (currency_name, currency_value, current_date)
    VALUES (?, ?, ?)
    """,
        (currency_name, currency_value, current_date),
    )
    connection.commit()


def main():
    # GET CURRENCY VAL
    data = get_exchange_rates()

    # GET EXCHANGErates and save to database
    # CODS: UAH = 980, USD = 840
    count = 0
    for item in data:
        if item["currencyCodeA"] == 840:
            if item["currencyCodeB"] == 980:  # UAH
                currency_name = "UAH"
                currency_value = item["rateBuy"]
                save_to_db(currency_name, currency_value)
                count += 1

    print("Exchange rates added to the database.")


main()
