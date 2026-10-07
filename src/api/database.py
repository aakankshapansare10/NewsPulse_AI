import psycopg2


DB_CONFIG = {
    "dbname": "newspulse_db",
    "user": "postgres",
    "password": "Postgres@5100",
    "host": "localhost",
    "port": "5100"
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)