import psycopg2

# Database connection parameters
conn_params = {
    'dbname': 'musicapp',
    'user': 'user_1',
    'password': 'test123',
    'host': 'localhost',
    'port': '5432'
}

# Read SQL file
with open('create_tables.sql', 'r') as file:
    sql_commands = file.read()

# Connect to the PostgreSQL database
conn = psycopg2.connect(**conn_params)
cur = conn.cursor()

try:
    # Execute the SQL commands
    cur.execute(sql_commands)
    conn.commit()
    print("Tables created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
    conn.rollback()
finally:
    # Close the cursor and connection
    cur.close()
    conn.close()
