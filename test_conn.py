import psycopg2
from dotenv import dotenv_values

config = dotenv_values("./.env")

try:
    connection = psycopg2.connect(
        user=config.get("DATABASE_USERNAME"),
        password=config.get("DATABASE_PASSWORD"),
        host=config.get("DATABASE_HOST"),
        port=config.get("DATABASE_PORT"),
        database=config.get("DATABASE_NAME")
    )
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")
