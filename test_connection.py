import psycopg2
from psycopg2 import sql

# Replace these with your actual RDS database credentials
db_config = {
    "host": "dbtest.cluster-cluwyikm8i9b.eu-north-1.rds.amazonaws.com",
    "port": "5432",  # default PostgreSQL port
    "dbname": "postgres",  # default database to connect to initially
    "user": "postgresMaster",
    "password": "pa55word"
}

try:
    # Connect to the default 'postgres' database
    connection = psycopg2.connect(**db_config)
    connection.autocommit = True
    cursor = connection.cursor()
    
    # Create a new database named 'primodatabase'
    cursor.execute("CREATE DATABASE primodatabase;")
    print("Database 'primodatabase' created successfully.")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
