import os
import mysql.connector
from mysql.connector import Error

# Database credentials from environment variables
host = os.environ['RDS_HOST']
port = os.environ['RDS_PORT']
database = os.environ['RDS_DATABASE']
user = os.environ['RDS_USER']
password = os.environ['RDS_PASSWORD']

# Initialize a dictionary to hold schema information and data
schema_info = {}

# Number of records to fetch from each table
record_limit = 5  # Adjust as needed

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)

        cursor = connection.cursor(dictionary=True)

        # Execute a query to fetch table names
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table['Tables_in_' + database]
            schema_info[table_name] = {"columns": [], "relationships": [], "excluded_columns": [], "data": []}

            # Fetch column details
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()

            # Process each column
            for column in columns:
                column_name = column['Field']
                column_type = column['Type']
                schema_info[table_name]["columns"].append({"name": column_name, "type": column_type})

                # Exclude byte data columns
                if 'blob' in column_type.lower():
                    schema_info[table_name]["excluded_columns"].append(column_name)

            # Fetch table data
            cursor.execute(f"SELECT * FROM {table_name} LIMIT {record_limit}")
            rows = cursor.fetchall()
            for row in rows:
                # Remove excluded columns from the row data
                for col in schema_info[table_name]["excluded_columns"]:
                    row.pop(col, None)
                schema_info[table_name]["data"].append(row)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

# Now, schema_info variable contains schema details and data named after each table
# You can print it to see the structure
print(schema_info)
