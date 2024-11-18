import psycopg2

db_params = {
    "dbname": "****",
    "user": "****",
    "password": "****",
    "host": "localhost",
    "port": "5432",
}


tables = [
    """
    CREATE TABLE Client (
    client_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        second_name VARCHAR(50) NOT NULL,
        card_number INTEGER NOT NULL,
        date_of_birth DATE,
        phone_number VARCHAR(15),
        email VARCHAR(100),
        address VARCHAR(255),
        branch INTEGER REFERENCES Branch(id),
        manager INTEGER REFERENCES Staff(staff_id)
    );
    """,
    """
    CREATE TABLE Account (
    id SERIAL PRIMARY KEY,
        client_id INTEGER NOT NULL REFERENCES Client(client_id),
        balance INTEGER NOT NULL,
        type_account VARCHAR(255),
        currency INTEGER NOT NULL,
        details_account VARCHAR(255) NOT NULL,
        contract_id INTEGER REFERENCES Contract(id)
    );
    """,
    """
    CREATE TABLE Account (
    id SERIAL PRIMARY KEY,
        client_id INTEGER NOT NULL REFERENCES Client(client_id),
        balance INTEGER NOT NULL,
        type_account VARCHAR(255),
        currency INTEGER NOT NULL,
        details_account VARCHAR(255) NOT NULL,
        contract_id INTEGER REFERENCES Contract(id)
    );
    """,
    """
    CREATE TABLE Cards (
    id SERIAL PRIMARY KEY,
        number VARCHAR(255) NOT NULL,
        expire_date DATE NOT NULL,
        cvv SMALLINT NOT NULL,
        card_type VARCHAR(255),
        account_id INT
    );
    """,
    """
    CREATE TABLE Invoice (
    id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        transaction_date TIMESTAMP NOT NULL,
        date_time TIMESTAMP,
        to_account_id INT NOT NULL,
        card_id INT,
        atm_id INT,
        terminal_id INT,
        amount DECIMAL NOT NULL,
        description VARCHAR(255),
        tax DECIMAL
    );
    """,
    """
    CREATE TABLE Staff (
    staff_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        second_name VARCHAR(50),
        email VARCHAR(100) UNIQUE,
        branch_id INTEGER REFERENCES Branch(branch_id),
        phone_number VARCHAR(15),
        date_of_birth DATE,
        position VARCHAR(100),
        address VARCHAR(100)
    );
    """,
    """
    CREATE TABLE Branch (
    branch_id SERIAL PRIMARY KEY,
        address VARCHAR(255),
        work_time TIMESTAMP,
        phone_number VARCHAR(15),
        administrator INTEGER REFERENCES Staff(staff_id)
    );
    """,
    """
    CREATE TABLE Currency_Rate (
    currency_rate_id SERIAL PRIMARY KEY,
        currency_from VARCHAR(255) NOT NULL,
        currency_to VARCHAR(255) NOT NULL,
        official_rate DECIMAL NOT NULL,
        date_time TIMESTAMP
    );
    """,
    """
    CREATE Tax Data (
    tax_data_id SERIAL PRIMARY KEY,
        tax_name VARCHAR(255) NOT NULL,
        account_id INT NOT NULL REFERENCES Currency_Rate(currency_rate_id,
        );
    """,
    """
    CREATE TABLE Partner (
    partner_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        contact_person VARCHAR(255),
        phone_number VARCHAR(15),
        email VARCHAR(100) UNIQUE,
        contract_id INTEGER,
        start_date DATE,
        end_date DATE,
        bank_account_id INTEGER,
        manager INT
        );    
    """,
    """
    CREATE TABLE Terminal (
    terminal_id SERIAL PRIMARY KEY,
        address VARCHAR(255),
        work_time TIMESTAMP,
        currency_id VARCHAR(255),
        card_id INTEGER
    );
    """,
    """
    CREATE TABLE ATM (
    atm_id SERIAL PRIMARY KEY,
        address VARCHAR(255),
        work_time TIMESTAMP,
        bank VARCHAR(255) NOT NULL,
        card_id INTEGER)
    """,
    """
    CREATE TABLE Contract (
    contract_id SERIAL PRIMARY KEY,
        contract_number VARCHAR(255) NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE,
        branch_id INTEGER REFERENCES Branch(branch_id),
        partner_id INTEGER REFERENCES Partner(partner_id)
    );
    """
]

with psycopg2.connect(**db_params) as connect:
    connect.autocommit = True
    with connect.cursor() as cursor:
        for query in tables:
            cursor.execute(query)
