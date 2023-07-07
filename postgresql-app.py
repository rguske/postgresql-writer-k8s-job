import os
import psycopg2

# Get the PostgreSQL connection information from environment variables
host = os.environ.get('POSTGRES_HOST')
port = os.environ.get('POSTGRES_PORT')
username = os.environ.get('POSTGRES_USERNAME')
password = os.environ.get('POSTGRES_PASSWORD')
database = os.environ.get('POSTGRES_DB')
table_name = os.environ.get('TABLE_NAME')
column1_name = os.environ.get('COLUMN_NAME1')
column2_name = os.environ.get('COLUMN_NAME2')

# Connect to the PostgreSQL database
conn = psycopg2.connect(host=host, port=port, user=username, password=password, dbname=database)
cur = conn.cursor()

# Example data to be inserted
data = [
    ('John', 'Doe'),
    ('Jane', 'Smith'),
    ('Alice', 'Johnson')
]

# SQL statement to insert data into the table
insert_query = f"INSERT INTO {table_name} ({column1_name}, {column2_name}) VALUES (%s, %s)"

# Execute the INSERT statement for each row of data
cur.executemany(insert_query, data)

# Commit the transaction and close the connection
conn.commit()
cur.close()
conn.close()