import psycopg2
from psycopg2 import sql

# Replace these with your actual RDS database credentials
db_config = {
    "host": "dbtest.cluster-ro-cluwyikm8i9b.eu-north-1.rds.amazonaws.com",
    "port": "5432",  # default PostgreSQL port
    "dbname": "dbTest",
    "user": "postgresMaster",
    "password": "pa55word"
}

try:
    # Establish a connection to the RDS database
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()

    # Run a simple query to check the connection
    cursor.execute("SELECT 1;")
    result = cursor.fetchone()

    if result:
        print("Connection successful! Database is accessible.")
    else:
        print("Connection failed. Check your credentials and network setup.")

except Exception as e:
    print(f"Error: {e}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Database connection closed.")