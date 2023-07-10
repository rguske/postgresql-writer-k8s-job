import os
import psycopg2

# Get the PostgreSQL connection information from environment variables
host = os.environ.get('POSTGRES_HOST')
port = os.environ.get('POSTGRES_PORT')
username = os.environ.get('POSTGRES_USERNAME')
password = os.environ.get('POSTGRES_PASSWORD')
database = os.environ.get('POSTGRES_DB')
table = os.environ.get('TABLE')
column1 = os.environ.get('COLUMN1')
column2 = os.environ.get('COLUMN2')

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
insert_query = f"INSERT INTO {table} ({column1}, {column2}) VALUES (%s, %s)"

# Execute the INSERT statement as well as the SEARCH query for each row of data
cur.executemany(insert_query, data)

# Execute the PostgreSQL search query
search_query = f"SELECT * FROM {table}"

# Execute the PostgreSQL search query
query = f"SELECT * FROM public.{table}"
cur.execute(query)

# Fetch all rows from the query result
rows = cur.fetchall()

# Print the rows to stdout
for row in rows:
    print(row)
    
# Commit the transaction and close the connection
conn.commit()
cur.close()
conn.close()
