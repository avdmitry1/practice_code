import sqlite3
import smtplib
from email.mime.text import MIMEText
from typing import List
from datetime import date


class Customer:
    def __init__(self, name: str, email: str, birthday: date):
        self.name = name
        self.email = email
        self.birthday = birthday

    def get_full_name(self):
        return f"{self.name}"

    def short_name(self):
        short_name = self.name.split()
        return f"{short_name[0]} {short_name[1][0]}.{short_name[2][0]}."

    def get_age(self):
        today = date.today()
        return today.year - self.birthday.year

    def __str__(self) -> str:
        return f"{self.get_full_name()}, {self.get_age()} years old"


def create_table():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS customers
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     email TEXT UNIQUE NOT NULL,
                     age INTEGER NOT NULL)"""
    )
    conn.commit()
    print("Table created successfully.")


def registration_new_user(customer: Customer):
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (name, email, age) VALUES (?,?,?)",
        (customer.get_full_name(), customer.email, customer.get_age()),
    )
    conn.commit()
    print(f"Sending greetings email to costumer {send_email()}")
    conn.close()


def send_email():
    # Create MIMEText object
    message = MIMEText(TEXT, "plain")
    message["Subject"] = "Greetings from our store!"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    # Send the email message
    with smtplib.SMTP(SERVER, PORT) as server:
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, TEXT.as_string())
        return customer.get_full_name()
    print(f"Sending email to costumer {send_email()}")


customer = Customer(
    "Avramenko Dmytro Borysovich", "avdmitry1@gmail.com", date(1987, 8, 21)
)


# Configuration mailtrap
SERVER = "live.smtp.mailtrap.io"
PORT = 586

USERNAME = "your_mailtrap_username"
PASSWORD = "your_mailtrap_password"

SENDER_EMAIL = "mailtrap@example.com"
RECEIVER_EMAIL = "new@example.com"

TEXT = f"""
    Dear {customer.get_full_name()},

    Thank you for registering at our store.

    We hope you will enjoy our products and services."""
