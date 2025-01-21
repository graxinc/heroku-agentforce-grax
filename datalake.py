import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
import pandas as pd


connection_string = os.getenv('GRAX_DATALAKE_URL')
def sql_connection():
    if not connection_string:
        raise ValueError("GRAX_DATALAKE_URL environment variable is not set")

    try:
        # Create the SQLAlchemy engine
        engine = create_engine(connection_string)
        # Establish the connection
        conn = engine.connect()
        return conn
    except Exception as e:
        raise Exception(f"Failed to connect to database: {str(e)}")

SQL_CONNECTION = sql_connection()
def query(query):
    try:
        return pd.read_sql_query(query, SQL_CONNECTION)
    except Exception as e:
        raise Exception(f"Query execution failed: {str(e)}")