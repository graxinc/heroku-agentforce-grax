import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
import pandas as pd

#connection_string = os.getenv('GRAX_DATALAKE_URL')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
SCHEMA_NAME = os.getenv('ATHENA_DATABASE')
AWS_REGION = os.getenv('AWS_REGION')
AWS_WORKGROUP = os.getenv('AWS_WORKGROUP', 'primary')
S3_STAGING_DIR = os.getenv('S3_STAGING_DIR')

conn_str = (
    "awsathena+rest://{aws_access_key_id}:{aws_secret_access_key}@"
    "athena.{region_name}.amazonaws.com:443/"
    "{schema_name}?s3_staging_dir={s3_staging_dir}&work_group={work_group}"
)

connection_string = conn_str.format(
    aws_access_key_id=quote_plus(AWS_ACCESS_KEY),
    aws_secret_access_key=quote_plus(AWS_SECRET_KEY),
    region_name=AWS_REGION,
    schema_name=SCHEMA_NAME,
    work_group=AWS_WORKGROUP,
    s3_staging_dir=quote_plus(S3_STAGING_DIR),
)

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