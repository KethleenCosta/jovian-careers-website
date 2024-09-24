# main.py

from database import db_connect
from sqlalchemy import text  # Import text for raw SQL queries

def load_jobs_from_db():
    # Get the engine and connection from db_connect
    engine, connection = db_connect()
    # Execute a raw SQL query using the connection object with `text()`
    result = connection.execute(text("SELECT * FROM jobs"))
    # Fetch and print the results
    jobs = []

    for row in result.all():
        jobs.append(dict(row._mapping)) # Use _mapping to convert to dict
    # Close the connection
    connection.close()

    return jobs
